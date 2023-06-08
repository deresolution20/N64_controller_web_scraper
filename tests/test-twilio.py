import os
from twilio.rest import Client

# Fetch sensitive data from environment variables
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ['TWILIO_PHONE']
to_phone = os.environ['TO_PHONE']

client = Client(twilio_account_sid, twilio_auth_token)
message = client.messages.create(body="This is a test SMS.", from_=twilio_phone, to=to_phone)
