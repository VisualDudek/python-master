# Usecase: Valiating Config Files
from typing import TypedDict

class Config(TypedDict):
    """
    A TypedDict for configuration settings.
    
    Attributes:
        name (str): The name of the configuration.
        log_level (str): The logging level for the configuration.
        retries (int): The number of retries for the configuration.
    """
    name: str
    log_level: str
    retries: int


def load_config(cfg: Config) -> None:
    """
    Load the configuration settings.
    
    Args:
        cfg (Config): The configuration settings to load.
    """
    assert cfg['log_level'] in ['DEBUG', 'INFO']

    
config_file: Config = {
    'name': 'example_config',
    'log_level': 'DEBUG',
    'retries': 3
}
load_config(config_file)