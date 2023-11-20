local awful = require('awful')
local wibox = require('wibox')
local style = require('ebenezer.style')

local function build(screen)
    screen.systray = wibox.widget {
        font = style.font_regular,
        widget = wibox.widget.systray
    }

    return wibox.container.margin(screen.systray)
end

local function setup_keybindings(modkey)
    awful.keyboard.append_global_keybindings({
        awful.key({modkey}, "=", function()
            awful.screen.focused().systray.visible =
                not awful.screen.focused().systray.visible
        end, {description = "Toggle systray visibility", group = "custom"})
    })
end

return {build = build, setup_keybindings = setup_keybindings}
