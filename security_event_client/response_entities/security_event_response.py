from typing import List

from security_event_client.response_entities.event import Event


class SecurityEventResponse:
    def __init__(self,
                 response_json,
                 ):
        self.customer_email = response_json.get('customer_email')
        self.number_of_events = response_json.get('number_of_events')
        self.events = [Event(**event) for event in response_json.get('events')]
