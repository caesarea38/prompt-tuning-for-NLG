import unittest
from os.path import join
from src.utils.config import load_config_from_yaml


class LoadConfigFromYamlTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.path_to_test_data = join(".", "src", "test", "data")

    def test_load_existing_yaml(self):
        expected = {"DATASET_PATH": "web_nlg", "DATASET_NAME": "release_v3.0_en"}
        config = load_config_from_yaml(join(self.path_to_test_data, "test_config.yml"))
        self.assertEqual(config, expected)

    def test_raises_error_file_not_exists(self):
        self.assertRaises(FileNotFoundError, load_config_from_yaml, "does_not_exist.file")

    def test_load_experiment_yaml(self):
        expected = {"DATASET_CONFIG": join("config", "web_nlg.yml")}
        config = load_config_from_yaml(join(self.path_to_test_data, "test_experiment.yml"))
        self.assertEqual(config, expected)
