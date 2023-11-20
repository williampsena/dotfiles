local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi

local markup = lain.util.markup

local icon_clear_sky = markup.fontfg(style.font_icon, style.fg_yellow, " ")
local icon_rainy = markup.fontfg(style.font_icon, style.fg_blue, " ")
local icon_clouds = markup.fontfg(style.font_icon, style.fg_orange, " ")

local function factory()
    local weather = lain.widget.weather({
        APPID = envs.weather_api_key,
        city_id = envs.city_id,
        font = style.font_light,
        settings = function()
            local description = weather_now["weather"][1]["description"]:lower()
            local units = math.floor(weather_now["main"]["temp"])

            if description == "clear sky" then
                description = icon_clear_sky
            elseif string.find(description, "rain") then
                description = icon_rainy
            elseif string.find(description, "clouds") then
                description = icon_clouds
            end

            widget:set_markup(description ..
                markup.fontfg(style.font_regular, style.fg_normal,
                    " " .. units .. "ºC"))
        end
    })

    return wibox.container.margin(wibox.widget {
        weather.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
