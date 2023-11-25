local awful = require('awful')
local wibox = require('wibox')
local naughty = require('naughty')
local lain = require("lain")
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local build_progressbar =
    require('ebenezer.helpers.progressbar').build_progressbar
local dpi = require('beautiful').xresources.apply_dpi

local colors = style.colors

local volume_enabled = "󰕾"
local volume_mute = "󰖁"
local notify_id = nil

local function get_volume_level(callback)
    awful.spawn.easy_async_with_shell(envs.commands.volume_level,
                                      function(volume_level, stderr, _reason,
                                               _existyletcode)
        callback(tonumber(volume_level))
    end)
end

local function notify_change_level(volumeicon)
    awful.spawn.easy_async_with_shell(envs.commands.volume_level,
                                      function(volume_level, stderr, _reason,
                                               _exitcode)

        get_volume_level(function(volume_level)
            local icon = volume_level == 0 and volume_mute or volume_enabled

            volumeicon:set_markup(icon)

            notify_id = naughty.notify({
                title = volume_enabled .. " Volume",
                font = style.font_strong,
                text = build_progressbar(volume_level, 10) .. " " ..
                    volume_level .. '%',
                position = 'top_right',
                bg = colors.bg_focus,
                fg = colors.fg_normal,
                margin = 10,
                width = 200,
                replaces_id = notify_id
            }).id
        end)
    end)
end

local function up_volume(volume, callback)
    get_volume_level(function(volume_level)
        if volume_level >= 99 then return end

        awful.spawn(
            string.format("pactl set-sink-volume %d +5%%", volume.device))

        callback()
    end)
end

local function factory()
    local volumeicon = wibox.widget {
        markup = volume_enabled,
        font = style.font_icon,
        valign = 'center',
        halign = "center",
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    local volume = lain.widget.pulsebar({font = style.font})

    local do_update = function(volume)
        volume.update()
        notify_change_level(volumeicon)
    end

    volumeicon:buttons(awful.util.table.join(
                           awful.button({}, 1, function() -- left click
            awful.spawn.with_shell("(pkill pavucontrol | true) && pavucontrol")
        end), awful.button({}, 2, function() -- middle click
            awful.spawn(string.format("pactl set-sink-volume %d 100%%",
                                      volume.device))
            do_update(volume)
        end), awful.button({}, 3, function() -- right click
            awful.spawn(string.format("pactl set-sink-mute %d toggle",
                                      volume.device))
            do_update(volume)
        end), awful.button({}, 4, function() -- scroll up
            up_volume(volume, function() 
                do_update(volume)
            end)
        end), awful.button({}, 5, function() -- scroll down
            awful.spawn(string.format("pactl set-sink-volume %d -5%%",
                                      volume.device))
            do_update(volume)
        end)))

    return wibox.container.margin(wibox.widget {
        volumeicon,
        volume.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

return factory
