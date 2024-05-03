import requests

from common.http_wrapper.entities.http_method import Method
from common.http_wrapper.entities.http_response import HttpResponse
from common.utils.retry import retry_on_server_error


def _verify_params(params):
    if not params:
        return {}
    else:
        return params


def _verify_headers(headers):
    if not headers:
        return {}
    else:
        return headers


def _post_method(url, body=None, data=None, params=None, headers=None):
    if data:
        return requests.post(url=url, data=data, params=params, headers=headers)
    elif body:
        return requests.post(url=url, json=body, params=params, headers=headers)


def _put_method(url, body, data, params, headers):
    if data:
        return requests.put(url=url, data=data, params=params, headers=headers)
    elif body:
        return requests.put(url=url, json=body, params=params, headers=headers)
    else:
        return requests.put(url=url, params=params, headers=headers)


def _delete_method(url, data, body, params, headers):
    if data:
        return requests.delete(url=url, data=data, params=params, headers=headers)
    elif body:
        return requests.delete(url=url, json=body, params=params, headers=headers)
    else:
        return requests.delete(url=url, params=params, headers=headers)


class HttpClient:

    @retry_on_server_error(max_retries=3, retry_interval=1)
    def send_request(self, url, method, body=None, data=None, params=None, headers=None) -> HttpResponse:
        params = _verify_params(params)
        headers = _verify_headers(headers)

        result = None
        if method == Method.GET:
            result = requests.get(url, params=params, headers=headers, timeout=10)

        elif method == Method.POST:
            result = _post_method(url, body, data, params, headers)

        elif method == Method.PUT:
            result = _put_method(url=url, body=body, data=data, params=params, headers=headers)

        elif method == Method.DELETE:
            result = _delete_method(url=url, body=body, data=data, params=params, headers=headers)

        return HttpResponse(result)
