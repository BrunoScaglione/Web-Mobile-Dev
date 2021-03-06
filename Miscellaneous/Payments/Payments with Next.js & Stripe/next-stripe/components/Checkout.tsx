import React from 'react';
import { loadStripe } from '@stripe/stripe-js';
import Stripe from 'stripe';

import stripeConfig from '../config/stripe'
// Make sure to call `loadStripe` outside of a component’s render to avoid
// recreating the `Stripe` object on every render.
const stripePromise = loadStripe(stripeConfig.publicKey);

interface Props {
  session: Stripe.Checkout.Session; 
}

const Checkout: React.FC<Props> = ({ session }) => {
  const handleClick = async (event) => {
    // Get Stripe.js instance
    const stripe = await stripePromise;
    
    // Call your backend to create the Checkout Session

    // When the customer clicks on the button, redirect them to Checkout.
    const result = await stripe.redirectToCheckout({
      sessionId: session.id,
    });

    if (result.error) {
      // If `redirectToCheckout` fails due to a browser or network
      // error, display the localized error message to your customer
      // using `result.error.message`.
    }
  };

  return (
    <button role="link" onClick={handleClick}>
      Buy
    </button>
  );
}

export default Checkout;
