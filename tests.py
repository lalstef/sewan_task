import pytest
from flask import Response
from sewan import app, notifiers


EMAIL_TARGET = 'test@example.com'
HTTP_TARGET = 'http://localhost:8003/test-notify/'

@pytest.fixture
def client():
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


# INTEGRATION TESTS

def test_notification_redispatched(client):
    response = client.post(
        '/api/v1.0/notification/', 
        data={'notification': 'test message'}, 
        headers={'Content-Type': 'application/json'}
    )
    assert response


# UNIT TESTS

def test_email_notifier_sends_email():
    email_notifier = notifiers.EmailNotifier(EMAIL_TARGET)
    message = email_notifier.notify('test message')
    assert message


def test_http_notifier_hits_the_url():
    http_notifier = notifiers.HTTPNotifier(HTTP_TARGET)
    response = http_notifier.notify('test message')
    assert response.status_code == 200