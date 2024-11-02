from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def get_layout_icon(layout_name):
    return ICONS.get(layout_name, "")


ICONS = {
    "monadtall": "󰕴",
    "monadwide": "󰜩",
    "max": "",
    "stack": "充",
    "columns": "",
    "floating": "",
    "tile": "",
}


class CurrentLayoutFontIcon(widget.CurrentLayout):
    """
    SDisplay the font icon related to the current layout of the current group of the screen,
    the bar containing the widget, is on.
    """

    def hook_response(self, layout, group):
        if group.screen is not None and group.screen == self.bar.screen:
            layout_icon = ICONS.get(layout.name, layout.name)
            self.text = f"{layout_icon} "
            self.bar.draw()


def build_current_layout_widget(settings: AppSettings, kwargs: dict):
    default_args = {
        "padding": 6,
        "scale": 0.6,
        "foreground": settings.colors.fg_normal,
        "background": settings.colors.bg_topbar_arrow,
        "font": settings.fonts.font_icon,
    }

    args = build_widget_args(settings, default_args, kwargs)
    type = kwargs.pop("widget_type", "font_icon")

    if type == "text":
        return widget.CurrentLayout(**args)
    elif type == "icon":
        return widget.CurrentLayoutIcon(**args)
    else:
        return CurrentLayoutFontIcon(**args)
