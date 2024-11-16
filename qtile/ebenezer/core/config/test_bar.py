from ebenezer.core.config.bar import AppSettingsBar
from ebenezer.core.config.loader import load_raw_test_settings


def test_parse_bar():
    settings = load_raw_test_settings()
    bar = AppSettingsBar(**settings.get("bar"))
    expected = AppSettingsBar(
        position="top",
        widgets=[
            {
                "type": "group_box",
                "margin_y": 3,
                "margin_x": 3,
                "padding": 3,
                "borderwidth": 3,
                "active": "fg_normal",
                "inactive": "fg_normal",
                "this_current_screen_border": "bg_topbar_selected",
                "this_screen_border": "fg_blue",
                "other_current_screen_border": "bg_topbar_selected",
                "highlight_color": "bg_topbar_selected",
                "highlight_method": "text",
                "foreground": "fg_normal",
                "rounded": False,
                "urgent_alert_method": "border",
                "urgent_border": "fg_urgent",
            },
            {
                "type": "separator",
            },
            {
                "type": "current_layout",
            },
        ],
    )

    assert bar.position == expected.position
    assert bar.widgets[0].__dict__ == expected.widgets[0].__dict__
    assert bar.widgets[1].__dict__ == expected.widgets[1].__dict__
    assert bar.widgets[2].__dict__ == expected.widgets[2].__dict__
