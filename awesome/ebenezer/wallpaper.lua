local awful = require('awful')
local wibox = require('wibox')
local gears = require('gears')
local envs = require('ebenezer.envs')
local fs = require('ebenezer.helpers.fs')

local function change_wallpaper(screen, wallpaper)
    local wallpaper_path = fs.resolve_path(wallpaper, envs.path_vars)
    gears.wallpaper.maximized(wallpaper_path, s, true)
end

local function setup_wallpaper(screen, wallpaper)
    local wallpaper = fs.resolve_path(wallpaper, envs.path_vars)

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

local function wallpaper_slideshow(screen)
    local wallpapers = fs.get_files(envs.environment.wallpaper_dir)
    local random_wallpaper = function()
        return wallpapers[math.random(1, #wallpapers)]
    end

    if next(wallpapers) == nil then return end

    setup_wallpaper(screen, random_wallpaper())

    local wallpaper_timeout = envs.environment.wallpaper_timeout or 600
    local wallpaper_timer = timer {timeout = wallpaper_timeout}

    wallpaper_timer:connect_signal("timeout", function()
        wallpaper_timer:stop() --       

        change_wallpaper(screen, random_wallpaper())

        wallpaper_timer.timeout = wallpaper_timeout
        wallpaper_timer:start()
    end)

    wallpaper_timer:start()
end

local function wallpaper_solo(screen)
    local wallpaper =
        fs.resolve_path(envs.environment.wallpaper, envs.path_vars)

    setup_wallpaper(screen, wallpaper)
end

function setup(screen)
    local slideshow_enabled = envs.environment.wallpaper_slideshow or "off"

    if slideshow_enabled == "on" then
        wallpaper_slideshow(screen)
    else
        wallpaper_solo(screen)
    end
end

return {setup = setup}
