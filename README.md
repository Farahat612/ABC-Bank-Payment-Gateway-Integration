# ABC-Bank-Payment-Gateway-Integration

An implementation of integrating PayPal and Stripe payment gateways into a Flask-based web application for American Bank of Commerce.

## Overview

The project aims to enhance the payment capabilities of American Bank of Commerce (ABC) by integrating PayPal and Stripe payment gateways into its online banking platform. This integration enables ABC's customers to securely make transactions using these popular payment methods. The project involves requirement gathering, gateway integration, and thorough testing.

## Features

- **PayPal Integration:** Allows users to make payments using the PayPal payment gateway.
- **Stripe Integration:** Provides functionality for making payments using the Stripe payment gateway.
- **Error Handling:** Implements robust error handling for API requests to enhance the reliability of the code.

## Repository Structure

- `/docs` : Contains project documentation.
- `/src` : Holds the source code for the integration.
- `/tests` : Includes test cases and automation scripts.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Gateway Integration](#gateway-integration)
- [Testing](#testing)
- [Logging](#logging)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)
- [License](#license)
- [Contact](#contact)

## Requirements

- Python 3.x
- [pip](https://pip.pypa.io/en/stable/installation/) installed
- Flask
- Requests library
- Stripe Python library
- PayPal Developer Account
- Stripe Developer Account
- dotenv library
- configparser library

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/Farahat612/ABC-Bank-Payment-Gateway-Integration..git
   ```

2. Navigate to the project directory:

   ```
   cd abc-payment-integration
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Update the `.env` file in the root directory and configure it with your API credentials:

   ```
   PAYPAL_CLIENT_ID=your_paypal_client_id
   PAYPAL_CLIENT_SECRET=your_paypal_client_secret
   STRIPE_PUBLIC_KEY=your_stripe_public_key
   STRIPE_SECRET_KEY=your_stripe_secret_key
   ```

2. Update `config.ini` with relevant configurations.

## Usage

1. Run the Flask application:

   ```
   python app.py
   ```

2. Access the application in your browser at http://localhost:5000.

## Gateway Integration

### PayPal Integration

Access the PayPal payment page by navigating to `/make_payment` and entering the amount.

### Stripe Integration

Access the Stripe payment page by navigating to `/make_stripe_payment`.

## Testing

1. Ensure you have testing dependencies installed:

   ```
   pip install -r tests/requirements-test.txt
   ```

2. Run tests:
   ```
   pytest tests/
   ```

### Logging

- Error logs are stored in the `payment_integration.log` file. Check this file for detailed information in case of any issues.

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests to us.

## Acknowledgments

- Thanks to [Flask](https://flask.palletsprojects.com/) for providing a lightweight and flexible web framework.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or support, please contact [Mohamed Farahat](mailto:mohamed.farahat97@proton.me).
