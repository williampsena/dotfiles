local awful = require('awful')
local wibox = require('wibox')
local lain = require("lain")
local style = require('ebenezer.style')
local dpi = require('beautiful').xresources.apply_dpi
local commands = require('ebenezer.envs').commands

local wifi_great = "󰤨 "
local wifi_good = "󰤨 "
local wifi_mid = "󰤢 "
local wifi_weak = "󰤟 "
local wifi_diconnected = "󰤯 "
local wifi_signal = 0
local wifi_signal_count = 0

--  nmcli -t -f name connection show --active

local function calculate_signal(current_wifi_signal)
    if wifi_signal == 0 then
        return current_wifi_signal
    else
        return (wifi_signal + current_wifi_signal) / 2
    end
end

local function bind_open_network_manager(net_icon)
    if commands.network_manager then
        net_icon:connect_signal("button::press", function(_, _, _, _)
            awful.spawn(commands.network_manager)
        end)
    end
end

local function factory()
    local net_icon = wibox.widget {
        markup = wifi_diconnected,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = wibox.widget.textbox
    }

    bind_open_network_manager(net_icon)

    local wifi_text = ""

    awful.tooltip {
        font = style.font_regular,
        objects = { net_icon },
        timer_function = function() return wifi_text end
    }

    local net = lain.widget.net({
        wifi_state = "on",
        eth_state = "on",
        settings = function()
            local wifi_device = net_now.devices.wlan0 or net_now.devices.wlp6s0

            wifi_text = "Received: " .. net_now.received .. "\n" .. "Sent: " ..
                net_now.sent

            if wifi_device then
                if wifi_device.wifi then
                    local signal = wifi_device.signal

                    wifi_signal = calculate_signal(signal)

                    -- waiting statistics
                    if wifi_signal_count <= 10 then
                        wifi_signal_count = wifi_signal_count + 1
                        return net_icon:set_markup(wifi_good)
                    end

                    if wifi_signal < -83 then
                        net_icon:set_markup(wifi_weak)
                    elseif wifi_signal < -70 then
                        net_icon:set_markup(wifi_mid)
                    elseif wifi_signal < -53 then
                        net_icon:set_markup(wifi_good)
                    elseif wifi_signal >= -53 then
                        net_icon:set_markup(wifi_great)
                    end

                    wifi_text = wifi_text .. "\nSignal: " ..
                        string.format("%.3f", wifi_signal)
                else
                    net_icon:set_markup(wifi_weak)
                end
            end
        end
    })

    return wibox.container.margin(wibox.widget {
        net_icon,
        net.widget,
        layout = wibox.layout.align.horizontal
    }, dpi(2), dpi(3))
end

return factory
