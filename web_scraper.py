# Import required libraries
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from twilio.rest import Client

# Fetch sensitive data from environment variables
# These are your Twilio account details and phone numbers
twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
twilio_phone = os.environ['TWILIO_PHONE']
to_phone = os.environ['TO_PHONE']

# Define a function to send SMS using Twilio API
def send_sms(body, to, from_, account_sid, auth_token):
    # Create a client for Twilio
    client = Client(account_sid, auth_token)
    # Send the SMS
    message = client.messages.create(body=body, from_=from_, to=to)

# Set options for the web driver (Chrome)
options = Options()
# We'll run Chrome in headless mode (without GUI)
options.headless = True

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=options)

# Go to the product page
driver.get('https://www.nintendo.com/store/products/nintendo-64-controller/')

# Start an infinite loop
while True:
    try:
        # Try to find the product availability element on the page and get its text
        availability = driver.find_element(By.XPATH, '//*[@id="main"]/section[1]/div/div[3]/div[3]/button/span').text
        # Print the product availability status
        print(f"Product availability: {availability}")
        # If the product is no longer sold out
        if availability != "Sold out":
            # Send an SMS alert
            send_sms(body="The product is now available.", to=to_phone, from_=twilio_phone, account_sid=twilio_account_sid, auth_token=twilio_auth_token)
            # Break the loop
            break
    # If an exception occurs (e.g., the element is not found)
    except Exception as e:
        # Print the exception
        print(f"Exception occurred: {e}")
    # Wait for 60 seconds before the next iteration
    sleep(60)
