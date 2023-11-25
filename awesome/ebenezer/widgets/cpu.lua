local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi

local colors = style.colors
local markup = lain.util.markup

local cpu_font_icon = ""

local cpu_low = markup.fontfg(style.font_icon, colors.fg_yellow, cpu_font_icon)
local cpu_avg = markup.fontfg(style.font_icon, colors.fg_orange, cpu_font_icon)
local cpu_high = markup.fontfg(style.font_icon, colors.fg_red, cpu_font_icon)

local function factory()
    local cpu_icon = wibox.widget {
        markup = cpu_font_icon,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    local cpu = lain.widget.cpu({
        font = style.font,
        settings = function()
            local cpu_usage = tonumber(cpu_now.usage)

            if cpu_usage >= 80 then
                cpu_icon:set_markup(cpu_high)
            elseif cpu_usage >= 50 then
                cpu_icon:set_markup(cpu_avg)
            else
                cpu_icon:set_markup(cpu_low)
            end

            widget:set_markup(markup.font(style.font_regular,
                " " .. cpu_now.usage .. "% "))
        end
    })

    return wibox.container.margin(wibox.widget {
        cpu_icon,
        cpu.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
