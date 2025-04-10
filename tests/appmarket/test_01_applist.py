import json

import pytest
import requests


@pytest.mark.P1
@pytest.mark.flaky(rerun=3, rerun_delay=2)
class TestAppList:

    def test_app_list(self, data_share_token):
        arcana_auth = data_share_token
        headers = {
            "Accept": "application/json, text/plain, /",
            "Arcana-Auth": "bearer " + arcana_auth,
            "Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
            "Connection": "keep-alive"
        }
        session = requests.session()
        response = session.request(
            method="GET",
            headers=headers,
            url="http://192.168.60.37:7088/arcana-llm-service/console/api/explore/apps",
        )
        print(response.text)