local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi
local envs = require('ebenezer.envs')

local wifi_great = "󰤨"
local wifi_good = "󰤨"
local wifi_mid = "󰤢"
local wifi_weak = "󰤟"
local wifi_diconnected = "󰤯"
local ethernet_on = "󰈀"

local wifi_signal = -100
local wifi_signal_count = 0
local network_name = nil

local function get_wifi_network_name()
    if network_name then return end

    awful.spawn.easy_async_with_shell(envs.commands.network_connected_name,
                                      function(current_network_name, stderr,
                                               _reason, _existyletcode)
        network_name = current_network_name:gsub("[\n\r]", " ")
    end)
end

local function calculate_signal(current_wifi_signal)
    local alpha = 0.2

    if wifi_signal == 0 then
        return current_wifi_signal
    else
        return wifi_signal * (1 - alpha) + current_wifi_signal * alpha
    end
end
local function bind_open_network_manager(net_icon)
    if envs.commands.network_manager then
        net_icon:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(envs.commands.network_manager)
        end)
    end
end

local function ethernet_connected(net_now)
    local eth0 = net_now.devices.eth0

    return eth0 and eth0.ethernet
end

local function get_ethernet_status(net_now, net_icon)
    local eth0 = net_now.devices.eth0

    net_icon:set_markup(ethernet_on)

    return
        "Internet access through cable\n" .. "Received: " .. net_now.received ..
            "\n" .. "Sent: " .. net_now.sent
end
local function get_wifi_status(net_now, net_icon)
    local wifi_device = net_now.devices.wlan0 or net_now.devices.wlp6s0

    local network_text = "Received: " .. net_now.received .. "\n" .. "Sent: " .. net_now.sent

    if wifi_device then
        if wifi_device.wifi then
            local signal = wifi_device.signal
            local waiting_statistics = wifi_signal_count <= 10

            wifi_signal = calculate_signal(signal)

            get_wifi_network_name()

            if waiting_statistics then
                wifi_signal_count = wifi_signal_count + 1
                net_icon:set_markup(wifi_good)
            else
                if wifi_signal < -80 then
                    net_icon:set_markup(wifi_weak)
                elseif wifi_signal < -70 then
                    net_icon:set_markup(wifi_mid)
                elseif wifi_signal < -60 then
                    net_icon:set_markup(wifi_good)
                else
                    net_icon:set_markup(wifi_great)
                end

                network_text = network_text .. "\nSignal: " .. string.format("%.1f dBm", wifi_signal)
            end

            if network_name then
                network_text = network_text .. "\nNetwork: " .. network_name
            end
        else
            network_name = nil
            net_icon:set_markup(wifi_weak)
        end
    end

    return network_text
end

local function factory()
    local net_icon = wibox.widget {
        markup = wifi_diconnected,
        font = style.font_icon,
        valign = 'center',
        halign = "center",
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    bind_open_network_manager(net_icon)

    local network_text = "Waiting status"

    awful.tooltip {
        font = style.font,
        objects = {net_icon},
        timer_function = function() return network_text end
    }

    local net = lain.widget.net({
        wifi_state = "on",
        eth_state = "on",
        settings = function()
            if ethernet_connected(net_now) then
                network_text = get_ethernet_status(net_now, net_icon)
            else
                network_text = get_wifi_status(net_now, net_icon)
            end
        end
    })

    return wibox.container.margin(wibox.widget {
        net_icon,
        net.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

return factory
