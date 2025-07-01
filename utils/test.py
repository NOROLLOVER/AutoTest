import json
import requests


def test_request() -> dict:
    url = "https://www.baidu.com"
    method = "GET"
    session = requests.session()
    response = session.request(method=method, url=url)
    result = response.text
    print(result)

    return {
        "result": result,
    }
from flask import Flask, request, jsonify
import pymysql

# def execute_sql(sql, connection_info):
#     connection = None
#     try:
#         host = connection_info.get("host", "localhost")
#         user = connection_info.get("user")
#         password = connection_info.get("password")
#         database = connection_info.get("database")
#         port = connection_info.get("port")
#         charset = connection_info.get("charset", "utf8mb4")
#
#     # 建立数据库链接
#     with connection.cursor() as cursor:
#
#     except Exception as e:
#         print(f"出现错误，异常：{e}")


import requests



def main(url: str, method: str, headers=None, **kwargs) -> dict:
    # 添加data参数接收body
    session = requests.Session()
    response = session.request(
        method=method,
        url=url,
        headers=headers,
        **kwargs  # 传递其他参数，如data/json等
    )
    # 检查HTTP状态码，非200状态码抛出异常
    response.raise_for_status()
    result = response.text
    return {
        "result": result,
        "status_code": response.status_code
    }
if __name__ == '__main__':
    main("https://www.baidu.com","GET","")




