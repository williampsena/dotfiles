local awful = require('awful')
local wibox = require('wibox')
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi
local naughty = require('naughty')

local icon_brightness_low = '󰃞 '
local icon_brightness_mid = '󰃟 '
local icon_brightness_high = '󰃠 '

local current_brightness_level = nil
local notify_id = nil

local function parse_brightness_level(stdout)
    return tonumber(string.format("%.0f", stdout))
end

local function get_brightness_icon(brightness_level)
    if brightness_level <= 10 then
        return icon_brightness_low
    elseif brightness_level <= 70 then
        return icon_brightness_mid
    else
        return icon_brightness_high
    end
end

local function build()
    local brighticon = wibox.widget {
        markup = '󰃟',
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox
    }

    local brightness_text = ""

    awful.tooltip {
        font = style.font,
        objects = {brighticon},
        timer_function = function() return brightness_text end
    }

    -- If you use xbacklight, comment the line with "light -G" and uncomment the line bellow
    -- local brightwidget = awful.widget.watch('xbacklight -get', 0.1,
    local brightwidget = awful.widget.watch(envs.commands.brightness_level, 0.1,
                                            function(widget, stdout, stderr,
                                                     exitreason, exitcode)
        local brightness_level = parse_brightness_level(stdout)
        local update_brightness_icon = get_brightness_icon(brightness_level)

        brightness_text = "Brightness level: " .. brightness_level .. "%"

        brighticon:set_markup(update_brightness_icon)
    end)

    return wibox.container.margin(wibox.widget {
        brighticon,
        brightwidget,
        layout = wibox.layout.align.horizontal,
        forced_width = dpi(envs.environment.icon_widget_with)
    }, dpi(0), dpi(0))
end

local function build_progressbar(level)
    local icon = ""
    local bar = ""
    local color = ""

    level = level / 20

    for i = 1, level do bar = bar .. icon end

    return bar
end

local function notify_brightness_level()
    awful.spawn.easy_async(envs.commands.brightness_level,
                           function(stdout, stderr, reason, exit_code)
        local brightness_level = parse_brightness_level(stdout)
        local brightness_icon = get_brightness_icon(brightness_level)

        if brightness_level == current_brightness_level then return end

        current_brightness_level = brightness_level

        notify_id = naughty.notify({
            title = brightness_icon .. " Brightness",
            font = style.font_strong,
            text = build_progressbar(brightness_level) .. " " ..
                brightness_level .. '%',
            position = 'top_right',
            bg = style.bg_focus,
            fg = style.fg_normal,
            margin = 10,
            replaces_id = notify_id
        }).id
    end)
end

local function setup_keybindings(modkey)
    awful.keyboard.append_global_keybindings({
        awful.key({}, "XF86MonBrightnessUp", function()
            awful.spawn.easy_async(envs.commands.brightness_level_up,
                                   function()
                notify_brightness_level()
            end)
        end, {description = "Brightness up", group = "Hotkeys"}),
        awful.key({}, "XF86MonBrightnessDown", function()
            awful.spawn.easy_async(envs.commands.brightness_level_down,
                                   function()
                notify_brightness_level()
            end)
        end, {description = "Brightness down", group = "Hotkeys"})
    })
end

return {build = build, setup_keybindings = setup_keybindings}
