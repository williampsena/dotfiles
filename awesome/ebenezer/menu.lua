local awful = require('awful')
local hotkeys_popup = require("awful.hotkeys_popup")
local envs = require('ebenezer.envs')

local function factory(beautiful)
    local awesome_menu = {
        {
            "Hotkeys",
            function()
                hotkeys_popup.show_help(nil, awful.screen.focused())
            end
        }, {"Manual", string.format("%s -e man awesome", terminal)}, {
            "Edit config",
            string.format("%s -e %s %s", terminal, editor, awesome.conffile)
        }, {"Restart", awesome.restart}, {"Quit", function()
            awesome.quit()
        end}
    }

    local main_menu = awful.menu({
        theme = {width = 300},
        items = {
            {"awesome", awesome_menu, beautiful.awesome_icon},
            {"open terminal", terminal},
            {
                "lock screen",
                function() awful.spawn.with_shell(envs.commands.lock_screen) end
            }
        }
    })

    local menu_launcher = awful.widget.launcher({
        image = beautiful.awesome_icon,
        menu = main_menu
    })

    return awesome_menu, main_menu, menu_launcher

end

return factory

