local awful = require('awful')
local hotkeys_popup = require("awful.hotkeys_popup")
local envs = require('ebenezer.envs')
local wallpaper = require('ebenezer.wallpaper')

local function build_menu_items(beautiful)
    local items = {
        {"awesome", awesome_menu, beautiful.awesome_icon},
        {"open terminal", terminal}
    }

    local slide_show_enabled = envs.environment.wallpaper_slideshow or "off"

    if slide_show_enabled == "on" then
        table.insert(items, {
            "change wallpaper",
            function()
                wallpaper.change_random_wallpaper(awful.screen.focused())
            end
        })
    end

    table.insert(items, {
        "lock screen",
        function() awful.spawn.with_shell(envs.commands.lock_screen) end
    })

    return items
end

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
        items = build_menu_items(beautiful)
    })

    local menu_launcher = awful.widget.launcher({
        image = beautiful.awesome_icon,
        menu = main_menu
    })

    return awesome_menu, main_menu, menu_launcher

end

return factory

