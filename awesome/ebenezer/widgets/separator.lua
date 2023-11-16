local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi

local markup = lain.util.markup

local function factory(icon)
    icon = icon or "  "

    local separator_icon = wibox.widget {
        markup = markup.fontfg(style.font_icon, style.fg_focus, icon),
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox
    }

    return wibox.container.margin(wibox.widget {
        separator_icon,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
