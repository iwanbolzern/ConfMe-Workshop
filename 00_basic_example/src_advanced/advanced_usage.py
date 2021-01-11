from pathlib import Path

from confme import BaseConfig, GlobalConfig


class DatabaseConfig(BaseConfig):
    host: str
    port: int
    user: str


class AdvancedConfig(GlobalConfig):
    name: str
    database: DatabaseConfig


# my application
if __name__ == '__main__':
    # load configuration
    config_folder = Path(__file__).parent / 'config'
    print(f'Using configuration folder: {config_folder.resolve()}')

    AdvancedConfig.register_folder(config_folder)
    my_config = AdvancedConfig.get()

    # use it
    print(f'Using database connection {my_config.database.host} '
          f'on port {my_config.database.port}')
