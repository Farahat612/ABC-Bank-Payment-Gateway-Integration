# Import necessary libraries
from flask import Flask, render_template, redirect, url_for
import requests
import os
from dotenv import load_dotenv
import logging
import configparser
import stripe

# Load environment variables from .env file
load_dotenv()

# Load configurations from a file
config = configparser.ConfigParser()
config.read('config.ini')

# Initialize Flask app
app = Flask(__name__)

# PayPal API endpoints
PAYPAL_API_BASE = "https://api.sandbox.paypal.com"  # We will Use "https://api.paypal.com" for live environment
TOKEN_ENDPOINT = "/v1/oauth2/token"
PAYMENT_ENDPOINT = "/v2/checkout/orders"

# Configure logging
logging.basicConfig(filename='payment_integration.log', level=logging.INFO)

# Set Stripe API key
stripe.api_key = os.getenv("STRIPE_SECRET_KEY")

# Function to obtain access token from PayPal
def get_access_token():
    url = PAYPAL_API_BASE + TOKEN_ENDPOINT
    headers = {'Accept': 'application/json', 'Accept-Language': 'en_US'}
    data = {'grant_type': 'client_credentials'}

    try:
        response = requests.post(url, auth=(os.getenv("PAYPAL_CLIENT_ID"), os.getenv("PAYPAL_CLIENT_SECRET")), data=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses

        access_token = response.json()['access_token']
        return access_token

    except requests.exceptions.RequestException as e:
        # Log the error
        logging.error(f"Error obtaining access token: {e}")
        return None

# Function to create a PayPal payment

def create_paypal_payment(access_token, amount):
    """
    Creates a PayPal payment using the provided access token and amount.

    Args:
        access_token (str): The access token for authenticating the request.
        amount (float): The amount of the payment.

    Returns:
        dict: The JSON response containing the payment details if successful, None otherwise.
    """
    url = PAYPAL_API_BASE + PAYMENT_ENDPOINT
    headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token}

    try:
        data = {
            "intent": "CAPTURE",
            "purchase_units": [
                {
                    "amount": {
                        "currency_code": "USD",
                        "value": str(amount)  
                    }
                }
            ]
        }

        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an exception for bad responses

        return response.json()

    except requests.exceptions.RequestException as e:
        # Log the error
        logging.error(f"Error creating PayPal payment: {e}")
        return None

# Function to create a Stripe payment
def create_stripe_payment():
    try:
        # Create a PaymentIntent on the server
        intent = stripe.PaymentIntent.create(
            amount=1000,  # Amount in cents
            currency='usd',
            payment_method_types=['card'],
        )
        return intent.client_secret

    except stripe.error.StripeError as e:
        # Log the error
        logging.error(f"Error creating Stripe payment: {e}")
        return None

# Define routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/make_payment', methods=['POST'])
def make_payment():
    # Obtain access token
    access_token = get_access_token()

    if access_token:
        # Extract the amount from the form input field
        amount = float(request.form['amount'])
        # Create a PayPal payment
        payment_response = create_paypal_payment(access_token, amount)

        if payment_response:
            # Redirect to the PayPal approval URL
            approval_url = next((link['href'] for link in payment_response['links'] if link['rel'] == 'approve'), None)

            if approval_url:
                return redirect(approval_url)
            else:
                return "Error: Approval URL not found in the PayPal response."

    return "Error obtaining access token."

@app.route('/make_stripe_payment', methods=['POST'])
def make_stripe_payment():
    # Create a Stripe payment
    client_secret = create_stripe_payment()

    if client_secret:
        return render_template('stripe_payment.html', client_secret=client_secret)

    return "Error creating Stripe payment."

if __name__ == '__main__':
    app.run(debug=True)
