import pytest

from configs.setting import FILE_PATH
from utils.apiutils import RequestBase
from utils.configParser import ConfigParse
from utils.parse_and_replace_variables import RequestsBase
from utils.sendRequests import SendRequests

from utils.yaml_handler import write_yaml, read_yaml, clear_yaml, get_extract_yaml
from utils.debugTalk import DebugTalk


@pytest.mark.run(order=1)
class TestLogin:
    api_info = read_yaml("../../data/api_info.yaml")

    @classmethod
    def test_login(cls):

        response = RequestBase.execute_test_cases(cls.api_info)
        # token = response["access_token"]
        token = DebugTalk().get_extract_data("token")
        print(token)


        # 断言token是否不为空，不为空写入extract_yaml
        assert token is not None
        if token is not None:
            file_path = FILE_PATH["extract"]
            clear_yaml(file_path=file_path)
            write_yaml({"token": token})
