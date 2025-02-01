from django.test import TestCase
from singletons.config_manager import ConfigManager


class ConfigManagerTest(TestCase):

    def test_singleton_behavior(self):
        # Create two instances of ConfigManager
        config1 = ConfigManager()
        config2 = ConfigManager()

        # Assert that both instances are the same (singleton behavior)
        self.assertIs(config1, config2)

    def test_set_and_get_setting(self):
        config = ConfigManager()

        # Set a setting
        config.set_setting("DEFAULT_PAGE_SIZE", 50)

        # Assert that the setting is stored correctly
        self.assertEqual(config.get_setting("DEFAULT_PAGE_SIZE"), 50)