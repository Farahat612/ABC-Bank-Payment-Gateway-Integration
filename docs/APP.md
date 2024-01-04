
## Payment Integration

This code is a Flask application that integrates PayPal and Stripe payment gateways. It provides the necessary functions and routes to integrate PayPal and Stripe payments into a Flask application.

### Code Breakdown

1. Import the necessary libraries, including Flask, requests, os, dotenv, logging, configparser, and stripe.

2. Load environment variables from a `.env` file using the `load_dotenv()` function.

3. Read configurations from a `config.ini` file using the `configparser` module.

4. Initialize the Flask application.

5. Define constants for PayPal API endpoints, including the base URL, token endpoint, and payment endpoint.

6. Configure logging to log payment integration-related information to a file named `payment_integration.log`.

7. Set the Stripe API key using the value from the environment variable `STRIPE_SECRET_KEY`.

8. Define the `get_access_token()` function to obtain an access token from PayPal. It sends a POST request to the PayPal API with the client ID and client secret and returns the access token.

9. Define the `create_paypal_payment()` function to create a PayPal payment. It sends a POST request to the PayPal API with the access token and payment details and returns the JSON response from the API.

10. Define the `create_stripe_payment()` function to create a Stripe payment. It uses the Stripe API to create a PaymentIntent with the specified amount, currency, and payment method types and returns the client secret for the payment.

11. Define route handlers for the home page (`/`), the payment submission page (`/make_payment`), and the Stripe payment submission page (`/make_stripe_payment`).

12. The `home()` route handler renders the `index.html` template.

13. The `make_payment()` route handler obtains the access token from PayPal, extracts the payment amount from the form input, creates a PayPal payment using the access token and amount, and redirects the user to the PayPal approval URL.

14. The `make_stripe_payment()` route handler creates a Stripe payment and renders the `stripe_payment.html` template with the client secret.

15. Run the Flask application in debug mode if the script is executed directly.
