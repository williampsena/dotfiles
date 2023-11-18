local awful = require('awful')
local wibox = require('wibox')
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi

local logout_popup = require(
                         "awesome-wm-widgets.logout-popup-widget.logout-popup")

local function factory()
    local logout_icon = wibox.widget {
        markup = "⏻",
        font = style.font_icon,
        align = 'center',
        valigtextboxn = 'center',
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    logout_icon:connect_signal("button::press", function(_, _, _, _)
        logout_popup.launch({
            onlock = function()
                awful.spawn.with_shell(envs.commands.lock_screen)
            end
        })
    end)

    return wibox.container.margin(wibox.widget {
        logout_icon,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

return factory
