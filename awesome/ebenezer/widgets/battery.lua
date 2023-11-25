local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi
local envs = require('ebenezer.envs')

local colors = style.colors
local markup = lain.util.markup

local battery_ok = markup.fontfg(style.font_icon, colors.fg_normal, '󰁹')
local battery_90 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂂')
local battery_80 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂁')
local battery_70 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂀')
local battery_60 = markup.fontfg(style.font_icon, colors.fg_normal, '󰁿')
local battery_50 = markup.fontfg(style.font_icon, colors.fg_normal, '󰁾')
local battery_40 = markup.fontfg(style.font_icon, colors.fg_normal, '󰁽')
local battery_30 = markup.fontfg(style.font_icon, colors.fg_yellow, '󰁽')
local battery_20 = markup.fontfg(style.font_icon, colors.fg_orange, '󰁻')
local battery_10 = markup.fontfg(style.font_icon, colors.fg_red, '󰁺')
local battery_full = markup.fontfg(style.font_icon, colors.fg_normal, '󰂄')
local battery_empty = markup.fontfg(style.font_icon, colors.fg_red, '󰂃')
local battery_error = markup.fontfg(style.font_icon, colors.fg_red, '󰂑')

local battery_ac_90 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂋')
local battery_ac_80 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂊')
local battery_ac_70 = markup.fontfg(style.font_icon, colors.fg_normal, '󰢞')
local battery_ac_60 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂉')
local battery_ac_50 = markup.fontfg(style.font_icon, colors.fg_normal, '󰢝')
local battery_ac_40 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂈')
local battery_ac_30 = markup.fontfg(style.font_icon, colors.fg_normal, '󰂇')
local battery_ac_20 = markup.fontfg(style.font_icon, colors.fg_orange, '󰂆')
local battery_ac_10 = markup.fontfg(style.font_icon, colors.fg_red, '󰢜')
local battery_ac_full = markup.fontfg(style.font_icon, colors.fg_normal, '󰂅')

local battery_text = ""

local function bind_open_power_manager(baticon)
    if envs.commands.power_manager then
        baticon:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(envs.commands.power_manager)
        end)
    end
end

local function factory()
    local baticon = wibox.widget {
        markup = battery_ok,
        font = style.font_icon,
        valign = 'center',
        halign = "center",
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    bind_open_power_manager(baticon)

    awful.tooltip {
        objects = {baticon},
        timer_function = function() return "Battery: " .. battery_text end
    }

    lain.widget.bat({
        battery = "BAT0",
        font = style.font,
        settings = function()
            local charging = bat_now.ac_status == 1 or bat_now.status ==
                                 "Charging"

            if bat_now.perc and tonumber(bat_now.perc) >= 99 then
                baticon:set_markup(charging and battery_ac_full or battery_full)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 90 then
                baticon:set_markup(charging and battery_ac_90 or battery_90)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 80 then
                baticon:set_markup(charging and battery_ac_80 or battery_80)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 70 then
                baticon:set_markup(charging and battery_ac_70 or battery_70)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 60 then
                baticon:set_markup(charging and battery_ac_60 or battery_60)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 50 then
                baticon:set_markup(charging and battery_ac_50 or battery_50)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 40 then
                baticon:set_markup(charging and battery_ac_40 or battery_40)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 30 then
                baticon:set_markup(charging and battery_ac_30 or battery_30)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 20 then
                baticon:set_markup(charging and battery_ac_20 or battery_20)
            elseif bat_now.perc and tonumber(bat_now.perc) >= 10 then
                baticon:set_markup(charging and battery_ac_10 or battery_10)
            elseif bat_now.perc and tonumber(bat_now.perc) <= 5 then
                baticon:set_markup(battery_empty)
            else
                baticon:set_markup(battery_error)
            end

            if charging then
                widget:set_markup(markup.font(style.font, " AC "))
                battery_text = "Charging " .. bat_now.perc .. "%"
            else
                widget:set_markup("")
                battery_text = markup.font(style.font,
                                           " " .. bat_now.perc .. "%")
            end
        end
    })

    return wibox.container.margin(wibox.widget {
        baticon,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

return factory
