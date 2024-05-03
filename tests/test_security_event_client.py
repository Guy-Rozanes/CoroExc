import pytest

import security_event_client.security_event_client


@pytest.mark.parametrize(
    'user_id', [
        1,
        2,
        3,
    ])
def test_get_event_of_user(
        user_id: int,
        security_event_client_api: security_event_client.security_event_client.SecurityEventClient,
):
    response = security_event_client_api.get_user_security_events(user_id)
    assert response.status_code == 200
    assert response.content.events != []


@pytest.mark.parametrize(
    'invalid_user_id',
    [
        'invalid_user',
        'as@#$sf',
        'u',
    ])
def test_get_event_of_invalid_user_id(
        security_event_client_api: security_event_client.security_event_client.SecurityEventClient,
        invalid_user_id: str,
):
    response = security_event_client_api.get_user_security_events(invalid_user_id)
    assert response.status_code == 400
    assert response.error.error_type != "user id is invalid"
