import unittest

from ebenezer.core.config.applications import AppSettingsApplications


class TestAppSettingsApplications(unittest.TestCase):

    def test_default_icons(self):
        app_settings = AppSettingsApplications()
        self.assertEqual(app_settings.icons, {})

    def test_custom_icons(self):
        custom_icons = {"firefox": "", "chrome": ""}
        app_settings = AppSettingsApplications(icons=custom_icons)
        self.assertEqual(app_settings.icons, custom_icons)


if __name__ == "__main__":
    unittest.main()
