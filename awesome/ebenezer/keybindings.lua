local awful = require('awful')
local naughty = require('naughty')
local microphone = require('ebenezer.widgets.microphone')
local brightness = require('ebenezer.widgets.brightness')
local systray = require('ebenezer.widgets.systray')
local screenshot = require('ebenezer.helpers.screenshot')
local envs = require('ebenezer.envs')
local modkey = envs.modkey

function setup(client)
    awful.keyboard.append_client_keybindings({
        awful.key({modkey}, "f", function(c)
            c.fullscreen = not c.fullscreen
            c:raise()
        end, {description = "toggle fullscreen", group = "client"}),
        awful.key({modkey, "Shift"}, "c", function(c) c:kill() end,
                  {description = "close", group = "client"}),
        awful.key({modkey, "Control"}, "space", awful.client.floating.toggle,
                  {description = "toggle floating", group = "client"}),
        awful.key({modkey, "Control"}, "Return",
                  function(c) c:swap(awful.client.getmaster()) end,
                  {description = "move to master", group = "client"}),
        awful.key({modkey}, "o", function(c) c:move_to_screen() end,
                  {description = "move to screen", group = "client"}),
        awful.key({modkey}, "t", function(c) c.ontop = not c.ontop end,
                  {description = "toggle keep on top", group = "client"}),
        awful.key({modkey}, "n", function(c)
            -- The client currently has the input focus, so it cannot be
            -- minimized, since minimized clients can't have the focus.
            c.minimized = true
        end, {description = "minimize", group = "client"}),
        awful.key({modkey}, "m", function(c)
            c.maximized_horizontal = not c.maximized_horizontal
            c.maximized_vertical   = not c.maximized_vertical
            c:raise()
        end, {description = "(un)maximize", group = "client"}),
        awful.key({modkey, "Control"}, "m", function(c)
            c.maximized_vertical = not c.maximized_vertical
            c:raise()
        end, {description = "(un)maximize vertically", group = "client"}),
        awful.key({modkey, "Shift"}, "m", function(c)
            c.maximized_horizontal = not c.maximized_horizontal
            c:raise()
        end, {description = "(un)maximize horizontally", group = "client"})

    })

    awful.keyboard.append_global_keybindings({
        awful.key({modkey, "Control"}, "c", function(c)
            awful.spawn.with_shell(envs.commands.lock_screen)
        end, {description = "Lock screen", group = "launcher"})
    })

    -- extra keybinds
    microphone.setup_keybindings(modkey)
    brightness.setup_keybindings(modkey)
    screenshot.setup_keybindings(modkey)
    systray.setup_keybindings(modkey)
end

return {setup = setup}
