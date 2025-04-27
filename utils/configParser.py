import configparser

from configs.setting import FILE_PATH


class ConfigParse:
    """
    解析ini后缀文件
    """

    def __init__(self, file_path=FILE_PATH["ini"]):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.read_config()

    def read_config(self):
        self.config.read(self.file_path)

    def get_value(self, section, option):
        """
        :param section: 获取头参数
        :param option: 获取下级key的值
        :return:
        """
        return self.config.get(section, option)

    def get_mysql(self,option):
        """
        获取mysql配置
        :param option:
        :return:
        """
        return self.config.get("Mysql",option)

if __name__ == '__main__':
    conf = ConfigParse()
    res = conf.get_value("Host","host")
    mq_res = conf.get_mysql("database")
    print(mq_res)