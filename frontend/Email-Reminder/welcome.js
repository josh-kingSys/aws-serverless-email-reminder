'use strict';

// Get the HTML elements this page needs. Each name describes its purpose.
var registrationForm = document.getElementById('registration-form');
var emailInput = document.getElementById('email');
var verifyButton = document.getElementById('verify-button');
var checkButton = document.getElementById('check-button');
var joshButton = document.getElementById('josh-button');
var statusMessage = document.getElementById('status');

// These functions are the ONLY places where you need to add API requests.
// They throw errors for now so the page never claims an email was verified.

async function requestEmailVerification(email) {
  // TODO: Call your API Gateway endpoint with this email address.
  // Your Lambda should ask SES to send its verification email.
  // Throw an Error if the request fails. Return when it is accepted.
  throw new Error('Email verification is not connected yet.');
}

async function checkEmailVerification(email) {
  // TODO: Call your backend to check this email address with SES.
  // Return true ONLY if the backend says it is verified; otherwise false.
  // Do not replace this with a permanent "return true" in the real app.
  throw new Error('Verification checking is not connected yet.');
}

function openReminderPage(recipient) {
  // Store the recipient so reminder.js can read it on the next page.
  // sessionStorage stores strings, so convert the object to JSON first.
  try {
    sessionStorage.setItem('emailReminderRecipient', JSON.stringify(recipient));
    window.location.href = 'reminder.html';
  } catch (error) {
    statusMessage.textContent = 'Browser storage is unavailable. Enable it and try again.';
  }
}

function setBusy(isBusy) {
  // Prevent duplicate requests or editing the address during a request.
  verifyButton.disabled = isBusy;
  checkButton.disabled = isBusy;
  joshButton.disabled = isBusy;
  emailInput.disabled = isBusy;
}

async function handleRegistration(event) {
  // Stop the form from reloading the page.
  event.preventDefault();
  var email = emailInput.value.trim();
  statusMessage.textContent = '';
  setBusy(true);

  try {
    // await pauses THIS function until the API operation finishes.
    await requestEmailVerification(email);
    statusMessage.textContent = 'Open the verification link in your email, then check verification here.';
  } catch (error) {
    statusMessage.textContent = error.message;
  } finally {
    // finally runs whether the request succeeds or fails.
    setBusy(false);
  }
}

async function handleVerificationCheck() {
  // Check required/email HTML rules before calling the backend.
  if (!registrationForm.reportValidity()) {
    return;
  }

  var email = emailInput.value.trim();
  statusMessage.textContent = '';
  setBusy(true);

  try {
    var verified = await checkEmailVerification(email);

    if (verified === true) {
      openReminderPage({ type: 'self', email: email });
    } else {
      statusMessage.textContent = 'This email is not verified yet.';
    }
  } catch (error) {
    statusMessage.textContent = error.message;
  } finally {
    setBusy(false);
  }
}

function handleSendToJosh() {
  // The backend will map "author" to Josh's configured email address.
  openReminderPage({ type: 'author' });
}

// Register the functions to run when the user submits or clicks.
registrationForm.addEventListener('submit', handleRegistration);
checkButton.addEventListener('click', handleVerificationCheck);
joshButton.addEventListener('click', handleSendToJosh);
