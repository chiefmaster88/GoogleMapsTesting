import requests
from logger import  Logger
'''Custom Https Methods'''


class HttpMethods:

    @staticmethod
    def post_method(url, body):
        Logger.add_request(url, method='POST')
        post_result = requests.post(url, json=body)
        Logger.add_response(post_result)
        return post_result

    @staticmethod
    def get_method(url):
        Logger.add_request(url, method='GET')
        get_result = requests.get(url)
        Logger.add_response(get_result)
        return get_result

    @staticmethod
    def put_method(url, body):
        Logger.add_request(url, method='PUT')
        put_result = requests.put(url, json=body)
        Logger.add_response(put_result)
        return put_result

    @staticmethod
    def delete_method(url, body):
        Logger.add_request(url, method='DELETE')
        delete_result = requests.delete(url, json=body)
        Logger.add_response(delete_result)
        return delete_result
