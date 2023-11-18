local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi

local volume_enabled = "󰕾"
local volume_mute = "󰖁"

local function factory()
    local volumeicon = wibox.widget {
        markup = volume_enabled,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    local volume = lain.widget.pulsebar({font = style.font})

    volumeicon:buttons(awful.util.table.join(
                           awful.button({}, 1, function() -- left click
            awful.spawn("pavucontrol")
        end), awful.button({}, 2, function() -- middle click
            volumeicon:set_markup(volume_mute)
            os.execute(string.format("pactl set-sink-volume %d 100%%",
                                     volume.device))
            volume.update()
        end), awful.button({}, 3, function() -- right click
            os.execute(string.format("pactl set-sink-mute %d toggle",
                                     volume.device))
            volume.update()
        end), awful.button({}, 4, function() -- scroll up
            os.execute(string.format("pactl set-sink-volume %d +1%%",
                                     volume.device))
            volume.update()
        end), awful.button({}, 5, function() -- scroll down
            os.execute(string.format("pactl set-sink-volume %d -1%%",
                                     volume.device))
            volume.update()
        end)))

    return wibox.container.margin(wibox.widget {
        volumeicon,
        volume.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

return factory
