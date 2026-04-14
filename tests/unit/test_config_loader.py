from packages.shared.settings.config_loader import ConfigLoader


def test_config_loader_reads_default_app_config() -> None:
    loader = ConfigLoader()
    config = loader.load_yaml("configs/app/default.yaml")

    assert config["app"]["name"] == "VoodoOS"
    assert config["app"]["api_port"] == 8000
