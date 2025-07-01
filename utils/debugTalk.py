import re
import random

from utils.yaml_handler import get_extract_yaml


class DebugTalk:

    def get_extract_data(self, node_name, out_format=None):
        """
        0 代表获取随机数，-1 代表获取所有数据，-2 代表将获取到的数据转换成列表
        :param node_name:
        :param out_format:
        :return:
        """
        data = get_extract_yaml(node_name)
        if out_format is not None and bool(re.compile(r"^[+-]?\d+$").match(str(out_format))):
            out_format = int(out_format)
            data_value = {
                out_format: self.seq_read(data, out_format),
                0: random.choice(data),
                -1: ','.join(data),
                -2: ','.join(data).split(',')
            }
            data = data_value[out_format]
        else:
            return get_extract_yaml(node_name, out_format)
        return data

    @classmethod
    def get_headers(cls, params_type):
        """
        获取请求头
        :param params_type:
        :return:
        """
        headers_mapping = {
            "data": {
                'Content-Type': "application/x-www-formurlencoded;charset=UTF-8",
                "authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0"
            },
            "json": {
                "Content-Type": "application/json;charset=UTF-8",
                "authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0"
            }
        }
        header = headers_mapping.get(params_type)
        if header is None:
            raise ValueError("不支持其它类型的请求头设置")
        return header

    def seq_read(self, data, randoms):
        if randoms not in [0, -1, -2]:
            return data[randoms - 1]
        else:
            return None


if __name__ == '__main__':
    print(DebugTalk().get_extract_data("token"))
