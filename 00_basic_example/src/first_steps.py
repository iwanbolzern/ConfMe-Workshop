from enum import Enum

from confme import BaseConfig
from confme.annotation import Secret


# config definition
# class DatabaseConnection(Enum):
#     TCP = 'tcp'
#     UDP = 'udp'


class DatabaseConfig(BaseConfig):
    host: str
    port: int
    # connection_type: DatabaseConnection
    user: str
    # password: str = Secret('highSecurePassword')


class MyConfig(BaseConfig):
    name: str
    database: DatabaseConfig


# my application
if __name__ == '__main__':
    # load configuration
    my_config = MyConfig.load('config.yaml')

    # use it
    print(f'Using database connection {my_config.database.host} '
          f'on port {my_config.database.port}')
