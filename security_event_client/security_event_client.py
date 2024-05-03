import common
from common.http_wrapper.entities.http_method import Method
from common.utils.retry import retry_on_server_error
from . import response_entities


class SecurityEventClient:

    def __init__(self, base_url: str = None) -> None:
        self.http_client = common.http_wrapper.http_wrapper.HttpClient()
        if not base_url:
            self.base_url = 'http://facebook.com'

    def get_user_security_events(self, user_id: int | str) -> response_entities.coro_custom_response.CoroCustomResponse:
        url = f'{self.base_url}/security-events/{user_id}'
        response = self.http_client.send_request(
            url=url,
            method=Method.GET,
        )
        return response_entities.coro_custom_response.CoroCustomResponse(response,
                                                                         response_entities.security_event_response.SecurityEventResponse)
