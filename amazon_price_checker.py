from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import ssl
import smtplib
from datetime import datetime, timedelta

good_message = """\
    From: {}
    To: {}
    Subject: Hi There! From Python Bot

    The price is lower than 30$, you should neet to consider to by it
    """
bad_message = """\
    From: {}
    To: {}
    Subject: Error
    
    There was an error in the authentication level, Pleas check the script
    """


def send_mail(message):
    # Description: Sending an email using SMTP with Python

    smtp_server = 'smtp.gmail.com'
    port = 465
    # Change This!
    sender = 'thesenderemail@gmail.com'

    # Description:
    # Go to your Gmail account, enable 2-factor authentication, and then create an app password.
    # This unique password will be retrieved from the environment variable set in the command prompt.
    # Open cmd command prompt, and save the password as an environment variable.
    # Don't forget to run this script from the same cmd window.

    password = os.getenv('EMAIL_PASSWORD')  # Retrieve password from environment variable
    # Change This!
    receiver = 'thereceiveremail@gmail.com'
    message = message.format(sender, receiver)

    context = ssl.create_default_context()

    # Establishing a secure SMTP connection
    try:
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender, password)  # Logging in to the SMTP server
            # Sending email
            server.sendmail(sender, receiver, message)
    except Exception as e:
        print(e)
        send_mail(bad_message)


# Function to calculate time until next 08:00
def time_until_next_eight():
    current_time = datetime.now()
    target_time = current_time.replace(hour=8, minute=0, second=0, microsecond=0)
    if current_time >= target_time:
        # If the current time is already past 08:00, schedule it for the next day
        target_time += timedelta(days=1)
    return (target_time - current_time).total_seconds()


on = True
while on:
    # Calculate time until next 08:00
    wait_time = time_until_next_eight()
    # Sleep until 08:00
    time.sleep(wait_time)
    # Set up WebDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")  # Add any other options you need

    driver = webdriver.Chrome()
    driver.get(
        "https://www.amazon.com/Razer-Ornata-Gaming-Keyboard-Low-Profile/dp/B09X6GJ691/ref=sr_1_2?dib=eyJ2IjoiMSJ9.yn0LBKrl5MYB8Znoxfb--0CDf879L3qZ121v4MbU3_xjxDSCjWNqICQTyd6Yq82Ca3JEwXYunvQYWbHi3-s7OkeeH3sMIMntEgovcj4DBzo_0d8IH9yo2t9y4uZHiQBtS8knaZs3amqN4XP4zx5rOFeXRPsk30TLUCwnkQM8Rrvw9iPL99UbgXbMMRuRlVgZFaw3O7S6Flw6pTN34e0XmZ9k0RtHj51xiaO8F1CksQk.dtSnQ5kBbwJkuvRXg5NhPPw_63IEtvZd4H__JaEi-_Q&dib_tag=se&keywords=gaming%2Bkeyboard&qid=1712470752&sr=8-2&th=1")
    price = driver.find_element(By.CLASS_NAME, "a-price-whole")
    price_value = price.text
    driver.quit()

    if int(price_value) < 30:
        send_mail(good_message)
        on = False
