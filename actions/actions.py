# Importing required modules
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class ActionSendEmail(Action):
    def name(self):
        return "action_send_email"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        try:
            # Extract the recipient's email address from the user's message
            recipient_email = None
            for entity in tracker.latest_message['entities']:
                if entity['entity'] == 'email':
                    recipient_email = entity['value']
                    break

            if recipient_email:
                # Set up email content
                subject = "Your Subject Here"
                body = "Your Email Body Here"

                # Create the email message
                message = MIMEMultipart()
                message['From'] = 'your_email@gmail.com'
                message['To'] = recipient_email
                message['Subject'] = subject
                message.attach(MIMEText(body, 'plain'))

                # Connect to the SMTP server and send the email
                with smtplib.SMTP('smtp.gmail.com', 587) as server:
                    server.starttls()
                    server.login('aadiltaitech@gmail.com', 'your_email_password')
                    server.sendmail('aadiltai3884@gmail.com', recipient_email, message.as_string())

                # Send a confirmation message to the user
                dispatcher.utter_message("Mail Sent")
            else:
                dispatcher.utter_message("I couldn't find a valid email address in your message.")

        except Exception as e:
            dispatcher.utter_message(f"An error occurred: {str(e)}")

        return []
