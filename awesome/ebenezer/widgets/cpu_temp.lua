local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi
local watch = require("awful.widget.watch")
local envs = require('ebenezer.envs')

local colors = style.colors
local markup = lain.util.markup

local temperature_ok = markup.fontfg(style.font_icon, colors.fg_light_blue,
                                     '󱃃')
local temperature_high = markup.fontfg(style.font_icon, colors.fg_red, '󱃂')

local function factory()
    local tempicon = wibox.widget {
        markup = temperature_ok,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    local temp = watch(envs.commands.cpu_thermal, 30,
                       function(widget, core_temperature)
        local update_tempicon = temperature_ok

        core_temperature = core_temperature:gsub("%s+", "")

        if tonumber(core_temperature) > 70 then
            update_tempicon = temperature_high
        end

        widget:set_markup(markup.font(style.font_regular,
                                      core_temperature .. "ºC"))
        tempicon:set_markup(update_tempicon)
    end)

    return wibox.container.margin(wibox.widget {
        tempicon,
        temp,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
