import pytest

from security_event_client.security_event_client import SecurityEventClient


@pytest.fixture(scope='module')
def security_event_client_api() -> SecurityEventClient:
    return SecurityEventClient()
