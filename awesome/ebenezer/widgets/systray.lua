local awful = require('awful')
local wibox = require('wibox')
local dpi = require('beautiful').xresources.apply_dpi
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')

local function build(screen)
    screen.systray = wibox.widget {
        widget = wibox.widget.systray,
        font = style.font_regular,
        halign = "center",
        base_size = dpi(envs.environment.icon_tray_widget_with),
        visible = false
    }

    local systray_with_background = wibox.container.background(screen.systray,
                                                               style.bg_systray 
    )

    return wibox.container.margin(systray_with_background, dpi(3), dpi(3),
                                  dpi(5), dpi(5))
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
