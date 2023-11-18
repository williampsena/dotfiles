local awful = require('awful')
local wibox = require('wibox')
local dpi = require('beautiful').xresources.apply_dpi
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')

local function factory(screen)
    local layoutbox = awful.widget.layoutbox {
        screen = screen,
        font = style.font,
        forced_width = dpi(envs.environment.icon_widget_with),
        buttons = {
            awful.button({}, 1, function() awful.layout.inc(1) end),
            awful.button({}, 3, function() awful.layout.inc(-1) end),
            awful.button({}, 4, function() awful.layout.inc(-1) end),
            awful.button({}, 5, function() awful.layout.inc(1) end)
        }
    }

    return wibox.container.margin(wibox.widget {
        layoutbox,
        layout = wibox.layout.align.horizontal
    }, dpi(10), dpi(3), dpi(3))
end

return factory
