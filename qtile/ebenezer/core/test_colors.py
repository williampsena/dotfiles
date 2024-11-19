import shutil
import tempfile
import unittest
from pathlib import Path

import yaml
from ebenezer.core.config.settings import AppSettings, AppSettingsColors
from ebenezer.core.theme import _apply_theme_color


class TestApplyThemeColor(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_apply_theme_color_file_exists(self):
        theme_filepath = Path(self.test_dir) / "theme.yaml"
        theme_data = {"colors": {"fg_black": "#FFFFFF", "fg_white": "#000000"}}
        with open(theme_filepath, "w") as f:
            yaml.dump(theme_data, f)

        settings = AppSettings(
            colors=AppSettingsColors(fg_black="#000000", fg_white="#FFFFFF")
        )

        updated_settings = _apply_theme_color(str(theme_filepath), settings)

        self.assertEqual(updated_settings.colors.fg_white, "#000000")
        self.assertEqual(updated_settings.colors.fg_black, "#FFFFFF")

    def test_apply_theme_color_file_not_exists(self):
        settings = AppSettings(
            colors=AppSettingsColors(fg_black="#FFFFFF", fg_white="#000000")
        )

        updated_settings = _apply_theme_color("non_existent_theme.yaml", settings)

        self.assertEqual(updated_settings.colors.fg_white, "#000000")
        self.assertEqual(updated_settings.colors.fg_black, "#FFFFFF")


if __name__ == "__main__":
    unittest.main()
