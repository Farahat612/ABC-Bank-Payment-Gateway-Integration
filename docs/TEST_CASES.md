# Test Cases

## PayPal Integration

### Test Case 1: Successful PayPal Payment

**Scenario:**

- User initiates a payment using PayPal.
- PayPal API returns a successful response.

**Expected Outcome:**

- User is redirected, and the status code is 302.

### Test Case 2: PayPal API Error

**Scenario:**

- User initiates a payment using PayPal.
- PayPal API returns an error response.

**Expected Outcome:**

- User sees an error message, and the status code is 500.

### Test Case 3: Successful PayPal Payment (Alternate Flow)

**Scenario:**

- User initiates a payment using PayPal.
- PayPal API returns a successful response.

**Expected Outcome:**

- User is redirected, and the status code is 302.

### Test Case 4: PayPal API Error (Alternate Flow)

**Scenario:**

- User initiates a payment using PayPal.
- PayPal API returns an error response.

**Expected Outcome:**

- User sees an error message, and the status code is 500.

## Stripe Integration

### Test Case 5: Successful Stripe Payment

**Scenario:**

- User initiates a payment using Stripe.
- Stripe API returns a successful response.

**Expected Outcome:**

- User is redirected, and the status code is 200.

### Test Case 6: Stripe API Error

**Scenario:**

- User initiates a payment using Stripe.
- Stripe API returns an error response.

**Expected Outcome:**

- User sees an error message, and the status code is 500.
