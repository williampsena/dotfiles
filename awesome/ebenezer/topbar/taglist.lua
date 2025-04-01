local wibox = require("wibox")
local gears = require("gears")
local envs = require("ebenezer.envs")
local modkey = envs.modkey
local awful = require('awful')
local lain = require('lain')
local style = require('ebenezer.style')

local function build_icon(icon) return " " .. icon .. " " end

local function build_table(screen)
    local tag_list = {}
    
    for icon in string.gmatch(envs.tags.list, "([^ ]+)") do
        table.insert(tag_list, build_icon(icon))
    end

    awful.tag(tag_list, screen, awful.layout.layouts[1])
end

function build_list(screen, client)
    return awful.widget.taglist {
        screen = screen,
        filter = awful.widget.taglist.filter.all,
        font = style.font_icon,
        buttons = {
            awful.button({}, 1, function(t) t:view_only() end),
            awful.button({modkey}, 1, function(t)
                if client.focus then client.focus:move_to_tag(t) end
            end), awful.button({}, 3, awful.tag.viewtoggle),
            awful.button({modkey}, 3, function(t)
                if client.focus then client.focus:toggle_tag(t) end
            end),
            awful.button({}, 4, function(t)
                awful.tag.viewprev(t.screen)
            end),
            awful.button({}, 5, function(t)
                awful.tag.viewnext(t.screen)
            end)
        }
    }
end

return {build_table = build_table, build_list = build_list}
