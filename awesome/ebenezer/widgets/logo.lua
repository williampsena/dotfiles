local awful = require('awful')
local wibox = require('wibox')
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')
local fs = require('ebenezer.helpers.fs')
local dpi = require('beautiful').xresources.apply_dpi

local default_icon = "$THEMES/icons/tux.png"

local function bind_click(logo)
    if envs.commands.click_logo then
        logo:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(envs.commands.click_logo)
        end)
    end
end

local function get_logo_path(logo) return fs.resolve_path(logo, envs.path_vars) end

local function factory()
    local icon = envs.environment.logo or default_config

    local logo_icon = wibox.widget {
        image = get_logo_path(icon),
        forced_width = dpi(18),
        forced_height = dpi(18),
        widget = wibox.widget.imagebox
    }

    bind_click(logo_icon)

    return wibox.container.margin(logo_icon, dpi(3), dpi(3), dpi(5), dpi(5))
end

return factory
