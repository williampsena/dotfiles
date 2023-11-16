local wibox = require('wibox')
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi

local default_icon = "{THEME_PATH}/icons/tux.png"

local function get_logo_path(logo)
    return logo:gsub("{THEME_PATH}", envs.theme_path)
end

local function factory()
    local icon = envs.environment.logo or default_config

    local logo_icon = wibox.widget {
        image = get_logo_path(icon),
        forced_width = dpi(18),
        forced_height = dpi(18),
        widget = wibox.widget.imagebox,
    }

    return wibox.container.margin(logo_icon, dpi(3), dpi(3), dpi(5), dpi(5))
end

return factory
