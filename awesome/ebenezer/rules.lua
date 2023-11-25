local awful = require('awful')
local envs = require('ebenezer.envs')

local tag_browser_index = envs.tags.browsers or 1
local tag_editors_index = envs.tags.editors or 3

local function setup(ruled)
    ruled.client.connect_signal("request::rules", function()
        -- All clients will match this rule.
        ruled.client.append_rule {
            id = "global",
            rule = {},
            properties = {
                focus = awful.client.focus.filter,
                raise = true,
                screen = awful.screen.preferred,
                placement = awful.placement.centered
            }
        }

        -- Floating clients.
        if envs.wm_class.floating then
            ruled.client.append_rule {
                id = "floating",
                rule_any = {
                    instance = {"copyq", "pinentry"},
                    class = envs.wm_class.floating,
                    -- Note that the name property shown in xprop might be set slightly after creation of the client
                    -- and the name shown there might not match defined rules here.
                    name = {
                        "Event Tester" -- xev.
                    },
                    role = {
                        "AlarmWindow", -- Thunderbird's calendar.
                        "ConfigManager", -- Thunderbird's about:config.
                        "pop-up", -- e.g. Google Chrome's (detached) Developer Tools.
                        "GtkFileChooserDialog" -- modals
                    }
                },
                properties = {floating = true}
            }
        end

        -- Add titlebars to normal clients and dialogs
        ruled.client.append_rule {
            id = "titlebars",
            rule_any = {type = {"normal"}},
            properties = {titlebars_enabled = true}
        }

        -- Disable titlebars for selected window classes
        if envs.wm_class.no_titlebars then
            ruled.client.append_rule {
                id = "no-titlebars",
                rule_any = {class = envs.wm_class.no_titlebars},
                properties = {titlebars_enabled = false}
            }
        end

        -- Set titlebars enabled to dialogs
        if envs.wm_class.dialog_titlebars then
            ruled.client.append_rule {
                id = "dialog",
                rule_any = {class = envs.wm_class.dialog_titlebars},
                properties = {titlebars_enabled = true}
            }
        end

        -- Set browsers to always map on the browser tag
        if envs.wm_class.browsers then
            ruled.client.append_rule {
                rule_any = {class = envs.wm_class.browsers},
                properties = {
                    screen = 1,
                    tag = awful.screen.focused().tags[tag_browser_index]
                }
            }
        end

        -- Set editors to always map on the editors tag.
        if envs.wm_class.editors then
            ruled.client.append_rule {
                rule_any = {class = envs.wm_class.editors},
                properties = {
                    screen = 1,
                    tag = awful.screen.focused().tags[tag_editors_index]
                }
            }
        end
    end)
end

return {setup = setup}
