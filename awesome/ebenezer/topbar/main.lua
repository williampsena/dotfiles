local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local tasklist = require('ebenezer.topbar.tasklist')
local style = require('ebenezer.style')

local merge_tables = require('ebenezer.helpers.table').merge_tables
local envs = require('ebenezer.envs')
local cpu_widget = require("ebenezer.widgets.cpu")
local mem_widget = require('ebenezer.widgets.memory')
local battery_widget = require('ebenezer.widgets.battery')
local brightness_widget = require('ebenezer.widgets.brightness').build
local cpu_temp_widget = require('ebenezer.widgets.cpu_temp')
local network_widget = require('ebenezer.widgets.network')
local logout_widget = require('ebenezer.widgets.logout')
local systray_widget = require('ebenezer.widgets.systray').build
local weather_widget = require('ebenezer.widgets.weather')
local volume_widget = require('ebenezer.widgets.volume')
local microphone_widget = require('ebenezer.widgets.microphone').build
local separator_widget = require('ebenezer.widgets.separator')
local pacman_widget = require('ebenezer.widgets.pacman')
local logo_widget = require('ebenezer.widgets.logo')
local layoutbox_widget = require('ebenezer.widgets.layoutbox')

local separators = lain.util.separators

local function wrap_arrow_background(color)
    return function(widget) return wibox.container.background(widget, color) end
end

local function supported_widgets(screen)
    local arrow_color = style.topbar_arrow .. 55
    local arrow_left = separators.arrow_left("alpha", arrow_color)
    local _arrow_widget = wrap_arrow_background(arrow_color)

    return {
        logo = function() return logo_widget() end,
        weather = function() return weather_widget() end,
        cpu_temp = function() return cpu_temp_widget() end,
        cpu = function() return cpu_widget() end,
        mem = function() return mem_widget() end,
        volume = function() return volume_widget() end,
        microphone = function() return microphone_widget() end,
        network = function() return network_widget() end,
        battery = function() return battery_widget() end,
        systray = function() return systray_widget(screen) end,
        pacman = function() return pacman_widget() end,
        brightness = function() return brightness_widget end,
        logout = function() return logout_widget() end,
        task_list = function() return tasklist.build(screen) end,
        tag_list = function() return screen.mytaglist end,
        layoutbox = function() return layoutbox_widget(screen) end,
        separator = function() return separator_widget() end,
        arrow_widget = _arrow_widget,
        arrow = function() return arrow_left end
    }
end

local function build_arrow_widget(arrow_widget_key, supported_widgets)
    local widget_key = arrow_widget_key:gsub("arrow_", "")

    local widget = supported_widgets[widget_key]

    if not widget then return nil end

    return function() return supported_widgets.arrow_widget(widget()) end
end

local function build_widgets_group(string_widgets, supported_widgets)
    local widgets = {}
    local widget

    for value in string.gmatch(string_widgets, "([^ ]+)") do
        widget = nil
        if string.find(value, "^arrow_") then
            widget = build_arrow_widget(value, supported_widgets)
        else
            widget = supported_widgets[value]
        end

        if widget then table.insert(widgets, widget()) end
    end

    return widgets
end

local function build(screen)
    screen.tasklist = tasklist.build(screen)

    -- Keyboard map indicator and switcher
    -- local mykeyboardlayout = awful.widget.keyboardlayout()

    -- Create a textclock widget
    local mytextclock = wibox.widget.textclock()

    local widgets = supported_widgets(screen)
    local left_widgets = merge_tables({layout = wibox.layout.fixed.horizontal},
                                      build_widgets_group(
                                          envs.topbar.left_widgets, widgets))
    local right_widgets = merge_tables({layout = wibox.layout.fixed.horizontal},
                                       build_widgets_group(
                                           envs.topbar.right_widgets, widgets))

    return awful.wibar {
        margins = 10,
        position = "top",
        bg = style.topbar, -- .. 55,
        height = 34,
        screen = screen,
        widget = {

            layout = wibox.layout.stack,
            {
                layout = wibox.layout.align.horizontal,
                left_widgets,
                nil,
                right_widgets
            },
            {
                mytextclock,
                valign = "center",
                halign = "center",
                layout = wibox.container.place
            }
        }
    }
end

return {build = build}
