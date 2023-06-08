# Web Scraper for Product Availability

This script is a Python-based web scraper that checks the availability of a product on the Nintendo store. If the product becomes available, it sends an SMS alert to the user's phone number.

## How it Works

The script utilizes Selenium, a tool for controlling a web browser through the program. It automates browser actions such as opening URLs and interacting with elements on the page. 

In this script, Selenium navigates to the product page and retrieves the text of the availability status of the product. If the product is available, it triggers the Twilio API to send an SMS alert.

The script runs in an infinite loop, constantly checking the product's status every minute until it becomes available.

## Prerequisites

Before you start, ensure you have the following installed:

- Python 3.6 or later
- Selenium library
- Twilio library
- ChromeDriver (ensure that it's in your PATH)

## Setup

To run the script, you need to set up some environment variables. These variables store sensitive information such as your Twilio account details and the phone number to which the alert should be sent.

You can set the environment variables in your system settings or store them in a `.env` file at the root of your project (you'll need to install the `python-dotenv` library and load the variables from the file into the environment).

The environment variables you need to set are:

- `TWILIO_ACCOUNT_SID`: Your Twilio Account SID
- `TWILIO_AUTH_TOKEN`: Your Twilio Auth Token
- `TWILIO_PHONE`: Your Twilio phone number (the number from which the SMS will be sent)
- `TO_PHONE`: The phone number to which the SMS will be sent

## Usage

Once you've set up your environment variables, you can run the script with the following command:

```bash
python scraper.py
