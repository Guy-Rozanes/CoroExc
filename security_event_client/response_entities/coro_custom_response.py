import json

from security_event_client.response_entities.error_response import ErrorResponse


class CoroCustomResponse:

    def __init__(self, http_response, model):
        self.error = None
        self.status_code = http_response.status_code
        if str(self.status_code)[0] != 2:
            self.error = ErrorResponse(
                **json.loads(http_response.content),
            )
        else:
            try:
                if not model:
                    self.content = http_response.content
                else:
                    self.content = model(**json.loads(http_response.content))

            except json.JSONDecodeError | KeyError:
                print("response returned as a string instead of json")
                self.content = http_response.content
