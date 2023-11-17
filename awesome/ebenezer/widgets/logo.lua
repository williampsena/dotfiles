local awful = require('awful')
local wibox = require('wibox')
local lain = require('lain')
local envs = require('ebenezer.envs')
local style = require('ebenezer.style')
local fs = require('ebenezer.helpers.fs')
local dpi = require('beautiful').xresources.apply_dpi

local markup = lain.util.markup

local default_image = "$THEMES/icons/tux.png"
local default_icon = ""

local function bind_click(logo)
    if envs.commands.click_logo then
        logo:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(envs.commands.click_logo)
        end)
    end
end

local function get_logo_path(logo) return fs.resolve_path(logo, envs.path_vars) end

local function build_icon()
    local icon = envs.environment.logo_icon or default_icon
    local color = envs.environment.logo_icon_color or style.fg_normal

    return wibox.widget {
        markup = markup.fontfg(style.font_icon, color, icon),
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        forced_width = dpi(35),
        forced_height = dpi(30),
        widget = wibox.widget.textbox
    }
end

local function build_image()
    local image = envs.environment.logo or default_image

    return wibox.widget {
        image = get_logo_path(image),
        halign = "center",
        forced_width = dpi(35),
        forced_height = dpi(30),
        widget = wibox.widget.imagebox
    }
end

local function factory()
    local widget = envs.environment.logo and build_image() or build_icon()

    bind_click(widget)

    return wibox.container.margin(widget, dpi(3), dpi(3), dpi(5), dpi(5))
end

return factory
