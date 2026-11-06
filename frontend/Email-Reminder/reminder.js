'use strict';

// Get each HTML element by its ID. No shorthand helper functions.
var reminderForm = document.getElementById('reminder-form');
var recipientText = document.getElementById('recipient');
var sendNowInput = document.getElementById('send-now');
var sendLaterInput = document.getElementById('send-later');
var scheduleFields = document.getElementById('schedule-fields');
var dateInput = document.getElementById('send-date');
var timeInput = document.getElementById('send-time');
var timezoneText = document.getElementById('timezone');
var customSubjectInput = document.getElementById('custom-subject');
var subjectFields = document.getElementById('subject-fields');
var subjectInput = document.getElementById('subject');
var messageInput = document.getElementById('message');
var sendButton = document.getElementById('send-button');
var statusMessage = document.getElementById('status');
var recipient = null;

async function submitReminder(reminder) {
  // TODO: Add fetch() here to POST the reminder to your API Gateway URL.
  // The reminder object contains:
  // recipientType: "self" or "author"
  // email: the user's email, or null for Josh (resolved by your backend)
  // subject: the custom subject, or null for your backend's default subject
  // message: the message text
  // sendAt: a UTC date/time string, or null for immediate delivery
  //
  // Match these field names to YOUR backend's request format.
  // If your backend expects waitSeconds, convert sendAt when submitting.
  // Check response.ok and throw an Error for a failed API request.
  // Return only after the backend accepts the reminder.
  // The backend must also validate recipients, verification and dates.
  throw new Error('Sending is not connected yet. No reminder was sent or scheduled.');
}

function loadRecipient() {
  try {
    var savedRecipient = sessionStorage.getItem('emailReminderRecipient');
    recipient = JSON.parse(savedRecipient);
  } catch (error) {
    recipient = null;
  }

  if (recipient && recipient.type === 'author') {
    recipientText.textContent = 'Josh';
  } else if (recipient && recipient.type === 'self' && typeof recipient.email === 'string' && recipient.email.trim() !== '') {
    recipientText.textContent = recipient.email;
  } else {
    recipient = null;
    statusMessage.textContent = 'Choose a recipient on the welcome page first.';
    sendButton.disabled = true;
  }
}

function updateTimingFields() {
  // checked is true when the "Send later" radio button is selected.
  var sendLater = sendLaterInput.checked;
  scheduleFields.hidden = !sendLater;
  dateInput.disabled = !sendLater;
  timeInput.disabled = !sendLater;
  dateInput.required = sendLater;
  timeInput.required = sendLater;
}

function updateSubjectField() {
  var useCustomSubject = customSubjectInput.checked;
  subjectFields.hidden = !useCustomSubject;
  subjectInput.disabled = !useCustomSubject;
  subjectInput.required = useCustomSubject;
}

function setMinimumDate() {
  // Date inputs require YYYY-MM-DD. Use the user's local date.
  var today = new Date();
  var year = today.getFullYear();
  var month = String(today.getMonth() + 1).padStart(2, '0');
  var day = String(today.getDate()).padStart(2, '0');
  dateInput.min = year + '-' + month + '-' + day;
}

async function handleReminderSubmit(event) {
  event.preventDefault();
  statusMessage.textContent = '';

  if (recipient === null) {
    statusMessage.textContent = 'Choose a recipient on the welcome page first.';
    return;
  }

  var message = messageInput.value.trim();
  if (message === '') {
    statusMessage.textContent = 'Enter a message.';
    messageInput.focus();
    return;
  }

  // null means no custom subject. Your backend can supply its default.
  var subject = null;
  if (customSubjectInput.checked) {
    subject = subjectInput.value.trim();
    if (subject === '') {
      statusMessage.textContent = 'Enter a subject or turn off the custom subject option.';
      subjectInput.focus();
      return;
    }
  }

  // null means send immediately. Otherwise, use a UTC timestamp.
  var sendAt = null;
  if (sendLaterInput.checked) {
    var selectedDate = new Date(dateInput.value + 'T' + timeInput.value);
    var selectedTimestamp = selectedDate.getTime();

    if (Number.isNaN(selectedTimestamp) || selectedTimestamp <= Date.now()) {
      statusMessage.textContent = 'Choose a date and time in the future.';
      dateInput.focus();
      return;
    }

    // Converts the local date/time to UTC for the backend.
    sendAt = selectedDate.toISOString();
  }

  var email = null;
  if (recipient.type === 'self') {
    email = recipient.email;
  }

  // Collect the form values in one object for the API function.
  var reminder = {
    recipientType: recipient.type,
    email: email,
    subject: subject,
    message: message,
    sendAt: sendAt
  };

  sendButton.disabled = true;
  try {
    await submitReminder(reminder);
    statusMessage.textContent = 'Reminder accepted.';
  } catch (error) {
    statusMessage.textContent = error.message;
  } finally {
    sendButton.disabled = false;
  }
}

// Show the device timezone so the user knows how the time is interpreted.
var timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
timezoneText.textContent = 'Timezone: ' + timezone;

sendNowInput.addEventListener('change', updateTimingFields);
sendLaterInput.addEventListener('change', updateTimingFields);
customSubjectInput.addEventListener('change', updateSubjectField);
reminderForm.addEventListener('submit', handleReminderSubmit);

// Set up the page when it first loads.
loadRecipient();
setMinimumDate();
updateTimingFields();
updateSubjectField();
