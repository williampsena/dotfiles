from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args
from libqtile import bar, hook, widget
from libqtile.widget import base


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


class CurrentLayoutFontIcon(base._TextBox):
    """
    SDisplay the font icon related to the current layout of the current group of the screen,
    the bar containing the widget, is on.
    """

    def __init__(self, width=bar.CALCULATED, **config):
        base._TextBox.__init__(self, "", width, **config)

    def _configure(self, qtile, bar):
        base._TextBox._configure(self, qtile, bar)
        layout_id = self.bar.screen.group.current_layout
        self.text = self._fetch_icon(self.bar.screen.group.layouts[layout_id].name)
        self.setup_hooks()

        self.add_callbacks(
            {
                "Button1": qtile.next_layout,
                "Button2": qtile.prev_layout,
            }
        )

    def hook_response(self, layout, group):
        if group.screen is not None and group.screen == self.bar.screen:
            self.text = self._fetch_icon(layout.name)
            self.bar.draw()

    def setup_hooks(self):
        hook.subscribe.layout_change(self.hook_response)

    def remove_hooks(self):
        hook.unsubscribe.layout_change(self.hook_response)

    def finalize(self):
        self.remove_hooks()
        base._TextBox.finalize(self)

    def _fetch_icon(self, layout_name: str):
        layout_icon = ICONS.get(layout_name, layout_name)
        return f"{layout_icon} "


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
