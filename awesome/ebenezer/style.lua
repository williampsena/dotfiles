local home = os.getenv("HOME")
local dpi = require("beautiful.xresources").apply_dpi
local style = {}

-- wallpaper
style.wallpaper = home .. "/Pictures/Wallpapers/active.jpg"

-- {{{ Styles
style.font  = "Inter Medium 10"
style.font_regular = "Inter Medium 9"
style.font_light = "Inter Light 10"
style.font_strong = "Inter 12"
style.font_strong_bold = "Inter Bold 12"
style.font_alternative = "Iosevka Nerd Font 10"
style.font_icon = "Material Icons 11"
style.font_icon_alternative = "Font Awesome 11"

-- {{{ Top bar

style.topbar = "#253237"
style.topbar_arrow = "#5c6b73"

-- {{{ Colors
style.fg_normal = "#e0fbfc"
style.fg_focus = "#C4C7C5"
style.fg_urgent = "#CC9393"
style.bg_normal = "#263238"
style.bg_focus = "#1E2320"
style.bg_urgent = "#424242"
style.bg_systray = style.bg_normal
style.bg_selected = "#5c6b73"
-- }}}

-- {{{ Borders
style.useless_gap = dpi(1)
style.border_width = dpi(1)
style.border_color_normal = "#9db4c0"
style.border_color_active = "#c2dfe3"
style.border_color_marked = "#CC9393"
-- }}}

-- {{{ Titlebars
style.titlebar_bg_focus = "#263238"
style.titlebar_bg_normal = "#253238"
-- }}}

-- {{{ Colors
style.fg_blue = "#304FFE"
style.fg_ligth_blue = "#B3E5FC"
style.fg_yellow = "#FFFF00"
style.fg_red = "#D50000"
style.fg_orange = "#FFC107"
style.fg_purple = "#AA00FF"
style.fg_purple2 = "#6200EA"
style.fg_green = "#4BC1CC"
-- }}}

return style
