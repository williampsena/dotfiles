class AppSettingsColors:
    fg_normal = "#fff"
    fg_focus = "#fff"
    fg_urgent = "#bababa"
    bg_normal = "#000"
    bg_focus = "#000"
    bg_urgent = "#5c6b73"
    bg_systray = "#5c6b73"
    bg_selected = "#5c6b73"
    fg_blue = "#bababa"
    fg_ligth_blue = "#bababa"
    fg_yellow = "#bababa"
    fg_red = "#bababa"
    fg_orange = "#bababa"
    fg_purple = "#bababa"
    fg_green = "#bababa"
    fg_gray = "#9db4c0"
    fg_black = "#000000"
    fg_white = "#ffffff"
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

    def __init__(self, **kwargs):
        self.fg_normal = kwargs.get("fg_normal", self.fg_normal)
        self.fg_focus = kwargs.get("fg_focus", self.fg_focus)
        self.fg_urgent = kwargs.get("fg_urgent", self.fg_urgent)
        self.bg_normal = kwargs.get("bg_normal", self.bg_normal)
        self.bg_focus = kwargs.get("bg_focus", self.bg_focus)
        self.bg_urgent = kwargs.get("bg_urgent", self.bg_urgent)
        self.bg_systray = kwargs.get("bg_systray", self.bg_systray)
        self.bg_selected = kwargs.get("bg_selected", self.bg_selected)
        self.fg_blue = kwargs.get("fg_blue", self.fg_blue)
        self.fg_ligth_blue = kwargs.get("fg_ligth_blue", self.fg_ligth_blue)
        self.fg_yellow = kwargs.get("fg_yellow", self.fg_yellow)
        self.fg_red = kwargs.get("fg_red", self.fg_red)
        self.fg_orange = kwargs.get("fg_orange", self.fg_orange)
        self.fg_purple = kwargs.get("fg_purple", self.fg_purple)
        self.fg_green = kwargs.get("fg_green", self.fg_green)
        self.fg_gray = kwargs.get("fg_gray", self.fg_gray)
        self.fg_black = kwargs.get("fg_black", self.fg_black)
        self.fg_white = kwargs.get("fg_white", self.fg_white)
        self.bg_topbar = kwargs.get("bg_topbar", self.bg_topbar)
        self.bg_topbar_selected = kwargs.get(
            "bg_topbar_selected", self.bg_topbar_selected
        )
        self.bg_topbar_arrow = kwargs.get("bg_topbar_arrow", self.bg_topbar_arrow)
        self.border_color_normal = kwargs.get(
            "border_color_normal", self.border_color_normal
        )
        self.border_color_active = kwargs.get(
            "border_color_active", self.border_color_active
        )
        self.border_color_marked = kwargs.get(
            "border_color_marked", self.border_color_marked
        )
        self.titlebar_bg_focus = kwargs.get("titlebar_bg_focus", self.titlebar_bg_focus)
        self.titlebar_bg_normal = kwargs.get(
            "titlebar_bg_normal", self.titlebar_bg_normal
        )
        self.taglist_bg_focus = kwargs.get("taglist_bg_focus", self.taglist_bg_focus)
        self.group_focus = kwargs.get("group_focus", self.group_focus)
        self.group_normal = kwargs.get("group_normal", self.group_normal)

    def get_color(self, color_name: str) -> str:
        if color_name.startswith("#"):
            return color_name

        return self.__dict__.get(color_name) or self.fg_normal
