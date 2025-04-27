import pytest
import requests

from utils.configParser import ConfigParse
from utils.sendRequests import SendRequests


# 设置用例标签
@pytest.mark.P1
# 失败用例重新跑，reruns参数设定重跑次数，reruns_delay设定每次重跑时间间隔
@pytest.mark.flaky(
    reruns=3,
    reruns_delay=2
)
# 设置用例优先级
@pytest.mark.run(order=1)
class TestIndex:

    def test_index(self, data_share_token):
        arcana_auth = data_share_token
        headers = {
            "accept": "application/json, text/plain, */*",
            "arcana-auth": "bearer " + arcana_auth,
            "authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
            "Connection": "keep-alive"
        }
        host = ConfigParse().get_value("Host", "host")
        port = ConfigParse().get_value("Host", "port")
        response = SendRequests().send_request(method="GET", headers=headers,
                                               url=host + ":" + port + "/arcana-llm-service/console/api/index",
                                               json=None)
        result = response.json()
        print(type(result), result)
        gpu = result["gpu"]
        assert gpu is not None
