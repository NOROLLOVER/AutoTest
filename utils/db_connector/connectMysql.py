from utils.configParser import ConfigParse
import pytest

conf = ConfigParse()

class TestConnectMysql:
    def __init__(self):
        self.connect_config = {
            "host": conf.get_mysql("db_host"),
            "port": int(conf.get_mysql("db_port")),
            "username": conf.get_mysql("username"),
            "password": conf.get_mysql("password"),
            "database": conf.get_mysql("database")
        }

    try:
        pass
    except Exception as e:
        print(f"{e}")

if __name__ == '__main__':
    print(TestConnectMysql().connect_config)