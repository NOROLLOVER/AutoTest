import json
import re

from utils.debugTalk import DebugTalk
from utils.yaml_handler import read_yaml


class RequestsBase:


    def parse_and_replace_variables(self, yml_data):
        """
        解析并替换YAML数据中的变量引用，如：${get_extract_data(goodsId,1)}
        :param yml_data: 解析的YAML数据
        :return: 返回的是dict类型
        """
        yml_data_str = yml_data if isinstance(yml_data, str) else json.dumps(yml_data, ensure_ascii=False)
        for _ in range(yml_data_str.count('${')):
            if '${' in yml_data_str and '}' in yml_data_str:
                start_index = yml_data_str.index('$')
                end_index = yml_data_str.index('}', start_index)
                variable_data = yml_data_str[start_index:end_index + 1]


                # 使用正则表达式提取函数名和参数
                match = re.match('\$\{(\w+)\((.*?)\)\}', variable_data)
                if match:
                    func_name, func_params = match.groups()
                    func_params = func_params.split(',') if func_params else []


                    # 使用面向对象反射getattr调用函数
                    extract_data = getattr(DebugTalk(), func_name)(*func_params)


                    # 使用正则表达式替换原始字符中的变量引用为调用后的结果
                    yml_data_str = re.sub(re.escape(variable_data), str(extract_data), yml_data_str)


        # 还原数据，将其转换为字典类型
        try:
            data = json.loads(yml_data_str)
        except json.JSONDecodeError:
            data = yml_data_str


        return data


if __name__ == '__main__':
    data = read_yaml('.././data/adduser.yaml')["account"][1]
    print(data)
    req = RequestsBase()
    res = req.parse_and_replace_variables(data)
    print(f'解析后：{res}')