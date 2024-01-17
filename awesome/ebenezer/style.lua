local home = os.getenv("HOME")
local envs = require('ebenezer.envs')
local dpi = require("beautiful.xresources").apply_dpi
local style = {}

-- {{{ Styles
style.font = envs.fonts.font
style.font_regular = envs.fonts.font_regular
style.font_light = envs.fonts.font_light
style.font_strong = envs.fonts.font_strong
style.font_strong_bold = envs.fonts.font_strong_bold
style.font_icon = envs.fonts.font_icon

-- {{{ Top bar

style.topbar = envs.colors.bg_topbar
style.topbar_arrow = envs.colors.bg_topbar_arrow

-- {{{ Borders
style.useless_gap = dpi(5)
style.border_width = dpi(2)
style.border_color_normal = envs.colors.border_color_normal
style.border_color_active = envs.colors.border_color_active
style.border_color_marked = envs.colors.border_color_marked
-- }}}

-- {{{ Titlebars
style.titlebar_bg_focus = envs.colors.titlebar_bg_focus
style.titlebar_bg_normal = envs.colors.titlebar_bg_normal
-- }}}

-- {{{ Colors
style.colors = envs.colors
-- }}}

-- {{{ Taglist
style.taglist_bg_focus = envs.colors.taglist_bg_focus
-- }}}

return style
