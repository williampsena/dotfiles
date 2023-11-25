local home = os.getenv("HOME")
local awesome_path = home .. "/.config/awesome"
local theme_path = awesome_path .. "/ebenezer/"
local config_file = awesome_path .. "/config.ini"
local global_themes_path = require("gears.filesystem").get_themes_dir()
local lip = require('ebenezer.helpers.ini')
local fs = require('ebenezer.helpers.fs')
local merge_tables = require('ebenezer.helpers.table').merge_tables
local split = require('ebenezer.helpers.table').split

local default_config = {
    modkey = "Mod4",
    weather_api_key = "",
    city_id = 0,
    theme_path = theme_path,
    awesome_path = awesome_path,
    global_themes_path = global_themes_path,
    environment = {tag_list = "  󰎪 󰎭 󰎱 󰎳"},
    tags = {first = "1", second = "2", third = "3"},
    icon_theme="Papirus",
    icon_widget_with = 30,
    commands = {
        lock_screen = 'systemctl suspend',
        brightness = 'light -G',
        brightness_level_up = 'xbacklight -inc 10',
        brightness_level_down = 'xbacklight -dec 10',
        power_manager = 'xfce4-power-manager -c',
        network_manager = 'nm-connection-editor',
        cpu_thermal = 'sensors | sed -rn "s/.*Core 0:\\s+.([0-9.]+).*/\1/p"'
    },
    topbar = {left_widgets = 'tag_list', right_widgets = 'arrow_layoutbox'},
    startup = {picom = "picom --config $THEMES/picom.conf"},
    wm_class = {browsers = "firefox", editors = "code-oss"},
    fonts = {
        font = "Inter Medium 10",
        font_regular = "Inter Medium 9",
        font_light = "Inter Light 10",
        font_strong = "Inter 12",
        font_strong_bold = "Inter Bold 12",
        font_icon = "Material Icons 11"
    },
    colors = {
        fg_normal = "#e0fbfc",
        fg_focus = "#C4C7C5",
        fg_urgent = "#CC9393",
        bg_normal = "#263238",
        bg_focus = "#1E2320",
        bg_urgent = "#424242",
        bg_systray = "#37444b",
        bg_selected = "#5c6b73",
        fg_blue = "#304FFE",
        fg_ligth_blue = "#B3E5FC",
        fg_yellow = "#FFFF00",
        fg_red = "#D50000",
        fg_orange = "#FFC107",
        fg_purple = "#AA00FF",
        fg_purple2 = "#6200EA",
        fg_green = "#4BC1CC",
        bg_topbar = "#253237",
        bg_topbar_arrow = "#5c6b73",
        border_color_normal = "#9db4c0",
        border_color_active = "#c2dfe3",
        border_color_marked = "#CC9393",
        titlebar_bg_focus = "#263238",
        titlebar_bg_normal = "#253238"
    },
    path_vars = {THEMES= theme_path:sub(1, -2), HOME = home, AWESOME = awesome_path}
}

local function build_wm_classes(wm_class)
    local wm_classes = {}

    for key, value in pairs(wm_class) do
        if value then wm_classes[key] = split(value, ' ') end
    end

    return wm_classes
end

local function get_config()
    if not fs.file_exists(config_file) then return default_config end

    local config = lip.load(config_file)
    local environment = config.environment or {}
    local user_config = merge_tables(default_config, environment)

    user_config.environment = merge_tables(default_config.environment,
                                           config.environment)
    user_config.tags = config.tags or default_config.tags
    user_config.commands =
        merge_tables(default_config.commands, config.commands)
    user_config.topbar = merge_tables(default_config.topbar, config.topbar)
    user_config.startup = merge_tables(default_config.startup, config.startup)
    user_config.wm_class = build_wm_classes(config.wm_class or
                                                default_config.wm_class)
    user_config.fonts = merge_tables(default_config.fonts, config.fonts)
    user_config.colors = merge_tables(default_config.colors, config.colors)

    return user_config
end

return get_config()
