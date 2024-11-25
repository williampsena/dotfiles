from typing import List


class AppSettingsColors:
    raw: dict = {}
    theme: str | None = None
    fg_normal = "#fff"
    fg_focus = "#fff"
    fg_urgent = "#bababa"
    bg_normal = "#000"
    bg_focus = "#000"
    bg_urgent = "#5c6b73"
    bg_systray = "#5c6b73"
    bg_selected = "#5c6b73"
    fg_blue = "#bababa"
    fg_light_blue = "#bababa"
    fg_yellow = "#bababa"
    fg_red = "#bababa"
    fg_orange = "#bababa"
    fg_purple = "#bababa"
    fg_green = "#bababa"
    fg_gray = "#9db4c0"
    fg_black = "#000000"
    fg_white = "#ffffff"
    fg_selected = "#000"
    bg_topbar = "#5c6b73"
    bg_topbar_selected = "#000"
    bg_topbar_arrow = "#5c6b73"
    border_color_normal = "#bababa"
    border_color_active = "#bababa"
    border_color_marked = "#bababa"
    titlebar_bg_focus = "#000"
    titlebar_bg_normal = "#000"
    taglist_bg_focus = "#5c6b73"
    group_focus = "#fff"
    group_normal = "#5c6b73"
    lock_screen_blank_color = "#00000000"
    lock_screen_clear_color = "#ffffff22"
    lock_screen_default_color = "#9db4c0"
    lock_screen_key_color = "#8a8ea800"
    lock_screen_text_color = "#4BC1CC"
    lock_screen_wrong_color = "#D50000"
    lock_screen_verifying_color = "#41445800"
    lock_screen_joke_foreground_color = "#000"
    lock_screen_joke_text_color = "#fff"
    rofi_background = "#000"
    rofi_background_alt = "#fff"
    rofi_foreground = "#fff"
    rofi_selected = "#5c6b73"
    rofi_active = "#4BC1CC"
    rofi_urgent = "#D50000"
    rofi_border = "#5c6b73"
    rofi_border_alt = "#9db4c0"

    def __init__(self, **kwargs):
        self.theme = kwargs.pop("theme", None)
        self.raw = kwargs
        self._bind_colors(
            kwargs,
            [
                "fg_normal",
                "fg_focus",
                "fg_urgent",
                "bg_normal",
                "bg_focus",
                "bg_urgent",
                "bg_systray",
                "bg_selected",
                "fg_blue",
                "fg_light_blue",
                "fg_yellow",
                "fg_red",
                "fg_orange",
                "fg_purple",
                "fg_green",
                "fg_gray",
                "fg_black",
                "fg_white",
                "fg_selected",
                "bg_topbar",
                "bg_topbar_selected",
                "bg_topbar_arrow",
                "group_normal",
                "group_focus",
                "border_color_normal",
                "border_color_active",
                "border_color_marked",
                "titlebar_bg_focus",
                "titlebar_bg_normal",
                "taglist_bg_focus",
                "lock_screen_blank_color",
                "lock_screen_default_color",
                "lock_screen_key_color",
                "lock_screen_text_color",
                "lock_screen_wrong_color",
                "lock_screen_verifying_color",
                "lock_screen_joke_foreground_color",
                "lock_screen_joke_text_color",
                "rofi_background",
                "rofi_background_alt",
                "rofi_foreground",
                "rofi_selected",
                "rofi_active",
                "rofi_urgent",
                "rofi_border",
                "rofi_border_alt",
            ],
        )

    def get_color(self, color_name: str) -> str:
        if color_name.startswith("#"):
            return color_name

        return self.__dict__.get(color_name) or self.fg_normal

    def _bind_colors(self, args: dict, colors: List[str]):
        for color in colors:
            setattr(self, color, args.get(color, getattr(self, color)))
