-------------------------------
--  "Zenburn" awesome theme  --
--    By Adrian C. (anrxc)   --
-------------------------------
local envs = require("ebenezer.envs")
local init = require("ebenezer.init")
local style = require("ebenezer.style")
local themes_path = envs.theme_path
local global_themes_path = envs.global_themes_path
local rnotification = require("ruled.notification")
local dpi = require("beautiful.xresources").apply_dpi

-- {{{ Main
local theme = style

theme.tasklist_disable_icon = true

-- There are other variable sets
-- overriding the default one when
-- defined, the sets are:
-- [taglist|tasklist]_[bg|fg]_[focus|urgent|occupied|empty|volatile]
-- titlebar_[normal|focus]
-- tooltip_[font|opacity|fg_color|bg_color|border_width|border_color]
-- Example:
-- theme.taglist_bg_focus = "#CC9393"
-- }}}

-- {{{ Widgets
-- You can add as many variables as
-- you wish and access them by using
-- beautiful.variable in your rc.lua
-- theme.fg_widget        = "#AECF96"
-- theme.fg_center_widget = "#88A175"
-- theme.fg_end_widget    = "#FF5656"
-- theme.bg_widget        = "#494B4F"
-- theme.border_widget    = "#3F3F3F"
-- }}}

-- {{{ Menu
-- Variables set for theming the menu:
-- menu_[bg|fg]_[normal|focus]
-- menu_[border_color|border_width]
theme.menu_height = dpi(20)
theme.menu_width = dpi(100)
theme.menu_font = style.font_strong
-- }}}

-- {{{ Icons
-- {{{ Taglist

theme.taglist_font = style.font_icon
theme.taglist_spacing = 0
theme.taglist_fg_focus = style.fg_normal
-- theme.taglist_bg_focus = style.bg_normal
-- theme.taglist_squares_resize = "false"
-- }}}

-- {{{ Misc
theme.awesome_icon = themes_path .. "awesome-icon.png"
theme.menu_submenu_icon = themes_path .. "default/submenu.png"
-- }}}

-- {{{ Layout
theme.layout_tile = themes_path .. "layouts/tile.png"
theme.layout_tileleft = themes_path .. "layouts/tileleft.png"
theme.layout_tilebottom = themes_path .. "layouts/tilebottom.png"
theme.layout_tiletop = themes_path .. "layouts/tiletop.png"
theme.layout_fairv = themes_path .. "layouts/fairv.png"
theme.layout_fairh = themes_path .. "layouts/fairh.png"
theme.layout_spiral = themes_path .. "layouts/spiral.png"
theme.layout_dwindle = themes_path .. "layouts/dwindle.png"
theme.layout_max = themes_path .. "layouts/max.png"
theme.layout_fullscreen = themes_path .. "layouts/fullscreen.png"
theme.layout_magnifier = themes_path .. "layouts/magnifier.png"
theme.layout_floating = themes_path .. "layouts/floating.png"
theme.layout_cornernw = themes_path .. "layouts/cornernw.png"
theme.layout_cornerne = themes_path .. "layouts/cornerne.png"
theme.layout_cornersw = themes_path .. "layouts/cornersw.png"
theme.layout_cornerse = themes_path .. "layouts/cornerse.png"
-- }}}

-- {{{ Titlebar
theme.titlebar_close_button_focus = themes_path ..
                                        "titlebar/close_focus.png"
theme.titlebar_close_button_normal = themes_path ..
                                         "titlebar/close_normal.png"

theme.titlebar_minimize_button_normal = global_themes_path ..
                                            "default/titlebar/minimize_normal.png"
theme.titlebar_minimize_button_focus = global_themes_path ..
                                           "default/titlebar/minimize_focus.png"

theme.titlebar_ontop_button_focus_active = themes_path ..
                                               "titlebar/ontop_focus_active.png"
theme.titlebar_ontop_button_normal_active = themes_path ..
                                                "titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_inactive = themes_path ..
                                                 "titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_inactive = themes_path ..
                                                  "titlebar/ontop_normal_inactive.png"

theme.titlebar_sticky_button_focus_active = themes_path ..
                                                "titlebar/sticky_focus_active.png"
theme.titlebar_sticky_button_normal_active = themes_path ..
                                                 "titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_inactive = themes_path ..
                                                  "titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_inactive = themes_path ..
                                                   "titlebar/sticky_normal_inactive.png"

theme.titlebar_floating_button_focus_active = themes_path ..
                                                  "titlebar/floating_focus_active.png"
theme.titlebar_floating_button_normal_active = themes_path ..
                                                   "titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_inactive = themes_path ..
                                                    "titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_inactive = themes_path ..
                                                     "titlebar/floating_normal_inactive.png"

theme.titlebar_maximized_button_focus_active = themes_path ..
                                                   "titlebar/maximized_focus_active.png"
theme.titlebar_maximized_button_normal_active = themes_path ..
                                                    "titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_inactive = themes_path ..
                                                     "titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_inactive = themes_path ..
                                                      "titlebar/maximized_normal_inactive.png"
-- }}}
-- }}}

-- Set different colors for urgent notifications.
rnotification.connect_signal('request::rules', function()
    rnotification.append_rule {
        rule = {urgency = 'critical'},
        properties = {bg = '#D50000', fg = '#ffffff'}
    }
end)

-- Startup
init.startup()

return theme

-- vim: filetype=lua:expandtab:shiftwidth=4:tabstop=8:softtabstop=4:textwidth=80
