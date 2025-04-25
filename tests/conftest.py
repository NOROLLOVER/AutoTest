import pytest
from utils.sendRequests import SendRequests
from utils.yaml_handler import write_yaml


@pytest.fixture(scope="session", autouse=False, params=["北京", "上海", "成都", "重庆"], ids=["BJ", "SH", "CD", "CQ"])
def data_share_params(request):
    return request.param


@pytest.fixture(scope="session", autouse=False)
def data_share_token(request):
    headers = {
        "accept": "application/json, text/plain, */*",
        "arcana-auth": "bearer",
        "content-type": "application/json",
        "authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
        "connection": "keep-alive"
    }
    data = {
        "username": "admin",
        "password": "25d55ad283aa400af464c76d713c07ad",
        "remember": False,
        "tenantId": "000000",
        "grant_type": "password",
        "scope": "all",
        "verify": "gAoSiglRxSRTwzO9nNuhMAvOZVu1/rcqJLZ9xwdjSz630b2ksdBNF+GXiD3R/kkAcir392f7AOoY8nGDTFXAdFGME09K7deP7/+ckLoFr6AdrVyL/u/Qds1U6yTuhTIRJgcTwTH/+ulpTa5WF7PwUu1p/uQ3L6fVs8TI4/TZfE7QUNlH8Lke734sHtfIGoiBvpiLd/6qtBxhmbLvEJsZY0KHhYVfV2QM+l7u+L5JkUO/rEUcufimJd15JMmoJG+ZhfTszKK7Ie4CiDqK95mSex5ryMVO8yAYY2fD9I+cc02cjYMa5VVFHr7ddrF7djNTrTqGFSFFNoTXs+tRMbC4pw=="
    }
    response = SendRequests().send_request(method="POST", url="http://192.168.60.37:7088/arcana-auth/oauth/token",
                                           headers=headers, json=data)
    access_token = str(response.json()['access_token'])
    write_yaml(response.json())
    return access_token
