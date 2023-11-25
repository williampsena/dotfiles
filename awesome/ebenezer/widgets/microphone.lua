local awful = require('awful')
local wibox = require("wibox")
local beautiful = require("beautiful")
local lain = require("lain")
local dpi = require('beautiful').xresources.apply_dpi
local style = require("ebenezer.style")
local envs = require("ebenezer.envs")
local widgets = {mic = require("ebenezer.widgets.mic")}

local colors = style.colors
local markup = lain.util.markup

local microphone_enabled =
    markup.fontfg(style.font_icon, colors.fg_normal, "")
local microphone_mute = markup.fontfg(style.font_icon, colors.fg_normal, "")

local function build()
    local microphone_icon = wibox.widget {
        markup = microphone_mute,
        font = style.font_icon,
        valign = 'center',
        halign = "center",
        widget = wibox.widget.textbox,
        forced_width = dpi(envs.environment.icon_widget_with)
    }

    beautiful.mic = widgets.mic({
        markup = microphone_mute,
        font = style.font_icon,
        align = 'center',
        valign = 'center',
        widget = microphone_icon,
        timeout = 10,
        settings = function(self)
            if self.state == "muted" then
                microphone_icon:set_markup(microphone_mute)
            else
                microphone_icon:set_markup(microphone_enabled)
            end
        end
    })

    return wibox.container.margin(wibox.widget {
        beautiful.mic,
        layout = wibox.layout.align.horizontal
    }, dpi(0), dpi(0))
end

local function setup_keybindings(modkey)
    awful.keyboard.append_global_keybindings({
        awful.key({modkey, "Shift"}, "p", function()
            beautiful.mic:toggle()
        end, {description = "Toggle microphone (amixer)", group = "Hotkeys"})
    })
end

local function startup() beautiful.mic:mute() end

return {build = build, startup = startup, setup_keybindings = setup_keybindings}
