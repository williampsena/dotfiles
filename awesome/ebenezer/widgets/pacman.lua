local wibox = require('wibox')
local pacman_widget = require('awesome-wm-widgets.pacman-widget.pacman')
local style = require('ebenezer.style')
local commands = require('ebenezer.envs').commands
local dpi = require('beautiful').xresources.apply_dpi

local ghost_icon = "󰊠"

local function factory()
    return wibox.container.margin(wibox.widget {
        pacman_widget({
            interval = 600, -- Refresh every 10 minutes
            popup_bg_color = style.bg_focus,
            popup_border_width = 1,
            popup_border_color = style.fg_normal,
            popup_height = 10, -- 10 packages shown in scrollable window
            popup_width = 300,
            polkit_agent_path = '/usr/bin/lxpolkit'
        }),
        font = style.font_regular,
        layout = wibox.layout.align.horizontal,
    }, dpi(2), dpi(3))
end

return factory
