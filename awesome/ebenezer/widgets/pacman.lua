local wibox = require('wibox')
local pacman_widget = require('awesome-wm-widgets.pacman-widget.pacman')
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi

local ghost_icon = "󰮯 "
local colors = style.colors

local function factory()

    local pacman_icon = wibox.widget {
        markup = ghost_icon,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    local widget = pacman_widget({
        interval = 600, -- Refresh every 10 minutes
        popup_bg_color = colors.bg_focus,
        popup_border_width = 1,
        popup_border_color = colors.fg_normal,
        popup_height = 10, -- 10 packages shown in scrollable window
        popup_width = 300,
        polkit_agent_path = '/usr/bin/lxpolkit'
    })

    local group = wibox.widget {
        pacman_icon,
        widget,
        font = style.font_regular,
        layout = wibox.layout.align.horizontal
    }

    return wibox.container.margin(wibox.widget {
        group,
        font = style.font_regular,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
