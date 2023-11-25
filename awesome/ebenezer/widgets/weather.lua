local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local envs = require('ebenezer.envs')
local dpi = require('beautiful').xresources.apply_dpi

local colors = style.colors

local markup = lain.util.markup

local icon_clear_sky = markup.fontfg(style.font_icon, colors.fg_orange, "󰖨")
local icon_few_clouds = markup.fontfg(style.font_icon, colors.fg_yellow, "")
local icon_clouds = markup.fontfg(style.font_icon, colors.fg_gray, "")
local icon_drizzle = markup.fontfg(style.font_icon, colors.fg_ligth_blue, "")
local icon_rain = markup.fontfg(style.font_icon, colors.fg_blue, "")
local icon_thunder = markup.fontfg(style.font_icon, colors.fg_yellow, "")
local icon_snow = markup.fontfg(style.font_icon, colors.fg_ligth_blue, "")
local icon_mist = markup.fontfg(style.font_icon, colors.fg_yellow, "")

local function factory()
    local weather = lain.widget.weather({
        APPID = envs.weather_api_key,
        city_id = envs.city_id,
        font = style.font_light,
        settings = function()
            local description = weather_now["weather"][1]["description"]:lower()
            local units = math.floor(weather_now["main"]["temp"])

            if string.find(description, "clear sky") then
                description = icon_clear_sky
            elseif string.find(description, "few clouds") then
                description = icon_few_clouds
            elseif string.find(description, "clouds") then
                description = icon_clouds
            elseif string.find(description, "drizzle") then
                description = icon_drizzle
            elseif string.find(description, "rain") then
                description = icon_rain
            elseif string.find(description, "thunder") then
                description = icon_thunder
            elseif string.find(description, "snow") then
                description = icon_snow
            end

            widget:set_markup(description .. " " ..
                markup.fontfg(style.font_regular, colors.fg_normal,
                    " " .. units .. "ºC"))
        end
    })

    return wibox.container.margin(wibox.widget {
        weather.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
