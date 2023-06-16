from twilio.rest import Client
from decouple import config


class SMS():
    def __init__(self):
        self.account_sid = config('TWILIO_SID')
        self.auth_token = config('TWILIO_AUTH_TOKEN')
        self.twilio_number = config('TWILIO_NUMBER')
        self.recipients = config('RECIPIENTS', default='').split(',')
        self.client = Client(self.account_sid, self.auth_token)

    def send(self, body):
        for recipient in self.recipients:
            message = self.client.messages.create(
                body=body,
                from_=self.twilio_number,
                to=recipient
            )
            print(message.sid)