local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi

local markup = lain.util.markup
local separators = lain.util.separators

local mem_icon_font = "󰄧 "

local mem_low = markup.fontfg(style.font_icon, style.fg_purple, mem_icon_font)
local mem_avg = markup.fontfg(style.font_icon, style.fg_purple2, mem_icon_font)
local mem_high = markup.fontfg(style.font_icon, style.fg_red, mem_icon_font)

local function factory()
    local mem_icon = wibox.widget {
        markup = mem_low,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox
    }

    local mem = lain.widget.mem({
        font = style.font,
        settings = function()
            if mem_now.perc >= 80 then
                mem_icon:set_markup(mem_high)
            elseif mem_now.perc >= 50 then
                mem_icon:set_markup(mem_avg)
            else
                mem_icon:set_markup(mem_low)
            end

            widget:set_markup(markup.font(style.font_regular,
                " " .. mem_now.used .. "MB "))
        end
    })

    return wibox.container.margin(wibox.widget {
        mem_icon,
        mem.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
