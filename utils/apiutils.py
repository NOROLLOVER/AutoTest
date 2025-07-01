import json
import re

from utils import debugTalk
from utils.configParser import ConfigParse
from utils.sendRequests import SendRequests
from utils.yaml_handler import read_yaml, write_yaml
from utils.debugTalk import DebugTalk


class RequestBase:

    def __init__(self):
        self.conf = ConfigParse()

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

    def execute_test_cases(self, api_info):

        try:
            # 处理baseInfo里面的数据
            url = api_info["baseInfo"]["url"]
            method = api_info["baseInfo"]["method"]
            data = api_info["testCases"][0]["data"]
            header = api_info["baseInfo"].get("header", None)
            cookies = api_info["baseInfo"].get("cookies", None)
            if header is not None:
                header = eval(self.parse_and_replace_variables(header)) if isinstance(header, str) else header
                print(header)
            if cookies is not None:
                cookies = eval(self.parse_and_replace_variables(cookies)) if isinstance(cookies, str) else cookies
                print(cookies)

            # 处理testCases里面的数据
            for testcase in api_info["testCases"]:
                case_name = testcase.pop("case_name")
                val_result = self.parse_and_replace_variables(testcase.get("validation"))
                validation = testcase.pop("validation")
                extract = testcase.get("extract", None)
                extract_list = testcase.pop("extract_list", None)
                print(testcase)
                for param_type, param_value in testcase.items():
                    if param_type == "data":
                        json = param_value
                        print(json)
                        host, port = ConfigParse().get_value("Host", "host"), ConfigParse().get_value("Host", "port")
                        url = host + ":" + port + url
                        response = SendRequests().execute_request(method="post",url=url,headers=header,json=json)
                        token = response.json()["access_token"]
                        write_yaml({"token": token})
                        print(self.parse_and_replace_variables(testcase.get("extract")))




        except Exception as e:
            print(f"接口请求异常，原因:{e}")


if __name__ == '__main__':
    api_info = read_yaml("../data/api_info.yaml")
    RequestBase().execute_test_cases(api_info)
