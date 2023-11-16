local home = os.getenv("HOME")
local envs = require('ebenezer.envs')
local dpi = require("beautiful.xresources").apply_dpi
local style = {}

-- wallpaper
style.wallpaper = home .. "/Pictures/Wallpapers/active.jpg"

-- {{{ Styles
style.font = envs.fonts.font
style.font_regular = envs.fonts.font_regular
style.font_light =  envs.fonts.font_light
style.font_strong = envs.fonts.font_strong
style.font_strong_bold = envs.fonts.font_strong_bold
style.font_icon = envs.fonts.font_icon

-- {{{ Top bar

style.topbar = envs.colors.bg_topbar
style.topbar_arrow = envs.colors.bg_topbar_arrow

-- {{{ Borders
style.useless_gap = dpi(1)
style.border_width = dpi(1)
style.border_color_normal = envs.colors.border_color_normal
style.border_color_active = envs.colors.border_color_active
style.border_color_marked = envs.colors.border_color_marked
-- }}}

-- {{{ Titlebars
style.titlebar_bg_focus = envs.colors.titlebar_bg_focus
style.titlebar_bg_normal = envs.colors.titlebar_bg_normal
-- }}}

-- {{{ Colors
style.fg_normal = envs.colors.fg_normal
style.fg_focus = envs.colors.fg_focus
style.fg_urgent = envs.colors.fg_urgent
style.bg_normal = envs.colors.bg_normal
style.bg_focus = envs.colors.bg_focus
style.bg_urgent = envs.colors.bg_urgent
style.bg_systray = envs.colors.bg_systray
style.bg_selected = envs.colors.bg_selected

style.fg_blue = envs.colors.fg_blue
style.fg_ligth_blue = envs.colors.fg_ligth_blue
style.fg_yellow = envs.colors.fg_yellow
style.fg_red = envs.colors.fg_red
style.fg_orange = envs.colors.fg_orange
style.fg_purple = envs.colors.fg_purple
style.fg_purple2 = envs.colors.fg_purple2
style.fg_green = envs.colors.fg_green
-- }}}

return style
