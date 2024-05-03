import pytest
import security_event_client.security_event_client


@pytest.fixture(scope='module')
def security_event_client_api() -> security_event_client.security_event_client.SecurityEventClient:
    return security_event_client.security_event_client.SecurityEventClient()
