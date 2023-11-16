local awful = require('awful')
local wibox = require('wibox')
local gears = require('gears')
local envs = require('ebenezer.envs')
local fs = require('ebenezer.helpers.fs')

local function change_wallpaper(wallpaper, screen)
    local wallpaper_path = fs.resolve_path(wallpaper, envs.path_vars)
    gears.wallpaper.maximized(wallpaper_path, screen, true)
end

local function wallpaper_slideshow(screen)
    local wallpapers = fs.get_files(envs.environment.wallpaper_dir)
    local random_wallpaper = function()
        return wallpapers[math.random(1, #wallpapers)]
    end

    if next(wallpapers) == nil then return end

    change_wallpaper(random_wallpaper(), screen)

    local wallpaper_timeout = envs.environment.wallpaper_timeout or 600
    local wallpaper_timer = timer {timeout = wallpaper_timeout}

    wallpaper_timer:connect_signal("timeout", function()
        wallpaper_timer:stop() --       

        change_wallpaper(random_wallpaper(), screen)

        wallpaper_timer.timeout = wallpaper_timeout
        wallpaper_timer:start()
    end)

    wallpaper_timer:start()
end

local function wallpaper_solo(screen)
    local wallpaper =
        fs.resolve_path(envs.environment.wallpaper, envs.path_vars)

    screen.connect_signal("request::wallpaper", function(s)
        awful.wallpaper {
            screen = s,
            widget = {
                {
                    image = wallpaper,
                    upscale = true,
                    downscale = true,
                    widget = wibox.widget.imagebox
                },
                valign = "center",
                halign = "center",
                tiled = false,
                widget = wibox.container.tile
            }
        }
    end)
end

function setup(screen)
    local slideshow_enabled = envs.environment.wallpaper_slideshow or "off"

    if slideshow_enabled == "on" then
        wallpaper_slideshow(awful.screen.focused())
    else
        wallpaper_solo(screen)
    end
end

return {setup = setup}
