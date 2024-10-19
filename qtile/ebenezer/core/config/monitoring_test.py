from ebenezer.core.config.loader import load_raw_test_settings
from ebenezer.core.config.monitoring import AppSettingsMonitoring


def test_parse_monitoring():
    settings = load_raw_test_settings()
    monitoring = AppSettingsMonitoring(**settings.get("monitoring"))
    expected = AppSettingsMonitoring(
        default_color="fg_normal",
        high_color="fg_orange",
        medium_color="fg_yellow",
        threshold_medium=70,
        threshold_high=90,
        burn=True,
    )

    assert monitoring.__dict__ == expected.__dict__
