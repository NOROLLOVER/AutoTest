from http.client import responses

import requests


class SendRequests:
    def send_request(self, **kwargs):
        """
        发起请求
        :param kwargs: 请求参数
        :return:
        """
        response = None
        try:
            session = requests.session()
            response = session.request(**kwargs)
        except requests.ConnectionError:
            print("请求链接异常")
        except Exception as e:
            print(f"请求异常，原因：{e}")
        return response

    def execute_request(self, method, url, headers, json):
        """
        实现请求
        :param method: 请求方法
        :param url: 请求url
        :param headers: 请求头
        :param json: 请求体json
        :return:
        """
        response = None
        try:
            response = self.send_request(method=method, url=url, headers=headers, json=json)

        except Exception as e:
            print(f"请求异常，原因：{e}")

        return response


if __name__ == '__main__':
    req = SendRequests()
    method = "GET"
    url = "http://192.168.60.37:7088/arcana-system/system/private/show/cfg/get"
    response = req.send_request(method=method, url=url, headers=None, json=None)
    print(response.json())
