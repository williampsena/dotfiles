import unittest

from local.core.config.keybindings import AppSettingsKeyBinding


class TestAppSettingsKeyBinding(unittest.TestCase):
    def test_init_with_all_arguments(self):
        kwargs = {
            "name": "test_name",
            "keys": "key1 key2",
            "action": "test_action",
            "command": "test_command",
        }
        binding = AppSettingsKeyBinding(**kwargs)
        self.assertEqual(binding.name, "test_name")
        self.assertEqual(binding.keys, ["key1", "key2"])
        self.assertEqual(binding.action, "test_action")
        self.assertEqual(binding.command, "test_command")

    def test_init_with_missing_arguments(self):
        kwargs = {"name": "test_name"}
        binding = AppSettingsKeyBinding(**kwargs)
        self.assertEqual(binding.name, "test_name")
        self.assertEqual(binding.keys, [""])
        self.assertEqual(binding.action, "")
        self.assertEqual(binding.command, "")

    def test_init_with_no_arguments(self):
        binding = AppSettingsKeyBinding()
        self.assertEqual(binding.name, "")
        self.assertEqual(binding.keys, [""])
        self.assertEqual(binding.action, "")
        self.assertEqual(binding.command, "")


if __name__ == "__main__":
    unittest.main()
