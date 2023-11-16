local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi
local commands = require('ebenezer.envs').commands

local markup = lain.util.markup

local battery_ok = markup.fontfg(style.font_icon, style.fg_normal, '󰁹')
local battery_90 = markup.fontfg(style.font_icon, style.fg_normal, '󰂂')
local battery_70 = markup.fontfg(style.font_icon, style.fg_normal, '󰂀')
local battery_50 = markup.fontfg(style.font_icon, style.fg_normal, '󰁿')
local battery_30 = markup.fontfg(style.font_icon, style.fg_normal, '󰁾')
local battery_full = markup.fontfg(style.font_icon, style.fg_normal, '󰂄')
local battery_low = markup.fontfg(style.font_icon, style.fg_yellow, '󰁻')
local battery_empty = markup.fontfg(style.font_icon, style.fg_red, '󰂃')
local battery_ac = markup.fontfg(style.font_icon, style.fg_normal, '󰂅 ')
local battery_error = markup.fontfg(style.font_icon, style.fg_red, '󰂑')

local battery_text = ""

local function bind_open_power_manager(baticon)
    if commands.power_manager then
        baticon:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(commands.power_manager)
        end)
    end
end

local function factory()
    local baticon = wibox.widget {
        markup = battery_ok,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox
    }

    bind_open_power_manager(baticon)

    awful.tooltip {
        objects = { baticon },
        timer_function = function() return "Battery: " .. battery_text end
    }

    lain.widget.bat({
        battery = "BAT0",
        font = style.font,
        settings = function()
            if bat_now.ac_status == 1 or bat_now.status == "Charging" then
                widget:set_markup(markup.font(style.font, " AC "))
                baticon:set_markup(battery_ac)
                battery_text = "AC"
                return
            elseif bat_now.perc and tonumber(bat_now.perc) >= 99 then
                baticon:set_markup(battery_full)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 90 then
                baticon:set_markup(battery_90)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 70 then
                baticon:set_markup(battery_70)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 50 then
                baticon:set_markup(battery_50)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 30 then
                baticon:set_markup(battery_30)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 15 then
                baticon:set_markup(battery_low)
            elseif bat_now.perc and tonumber(bat_now.perc) <= 5 then
                baticon:set_markup(battery_empty)
            else
                baticon:set_markup(battery_error)
            end

            battery_text = markup.font(style.font, " " .. bat_now.perc .. "%")
            widget:set_markup("")
        end
    })

    return wibox.container.margin(wibox.widget {
        baticon,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
