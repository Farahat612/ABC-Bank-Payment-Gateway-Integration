# tests/test_integration.py
import pytest
import requests_mock
from src import app  

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_paypal_integration_success(client):
    # Mock the PayPal API endpoint
    with requests_mock.mock() as m:
        m.post('https://api.sandbox.paypal.com/v1/oauth2/token', json={'access_token': 'fake_token'})
        m.post('https://api.sandbox.paypal.com/v2/checkout/orders', json={'status': 'created'})

        # Make a request to the Flask app
        response = client.post('/make_payment')

    # Assert the expected outcome
    assert response.status_code == 302  # Assuming you're redirecting on success

def test_paypal_integration_error(client):
    # Mock the PayPal API endpoint to simulate an error
    with requests_mock.mock() as m:
        m.post('https://api.sandbox.paypal.com/v1/oauth2/token', status_code=500)

        # Make a request to the Flask app
        response = client.post('/make_payment')

    # Assert the expected outcome
    assert response.status_code == 500
    assert b"Error" in response.data  # Assuming you're displaying an error message

def test_stripe_integration_success(client):
    # Mock the Stripe API endpoint
    with requests_mock.mock() as m:
        m.post('https://api.stripe.com/v1/payment_intents', json={'client_secret': 'fake_secret'})

        # Make a request to the Flask app
        response = client.post('/make_stripe_payment')

    # Assert the expected outcome
    assert response.status_code == 200  # Assuming you're rendering a template

def test_stripe_integration_error(client):
    # Mock the Stripe API endpoint to simulate an error
    with requests_mock.mock() as m:
        m.post('https://api.stripe.com/v1/payment_intents', status_code=500)

        # Make a request to the Flask app
        response = client.post('/make_stripe_payment')

    # Assert the expected outcome
    assert response.status_code == 500
    assert b"Error" in response.data  # Assuming you're displaying an error message
