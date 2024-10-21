from libqtile import widget

from ebenezer.core.config.settings import AppSettings
from ebenezer.widgets.helpers.args import build_widget_args


def build_current_layout_widget(settings: AppSettings, kwargs: dict):
    default_args = {"padding": 5, "scale": 0.6}
    args = build_widget_args(settings, default_args, kwargs, [])

    return widget.CurrentLayoutIcon(**args)
