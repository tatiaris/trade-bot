from twilio.rest import Client
import decouple
from decouple import config


def send_text(msg: str) -> str:
    """ Sends a text message to recipient phone number """

    # Get Environment Variables
    try:
        account_sid = config('TWILIO_ACCOUNT_SID')
        auth_token = config('TWILIO_AUTH_TOKEN')
        twilio_phone_number = config('TWILIO_PHONE_NUMBER')
        my_phone_number = config('MY_PHONE_NUMBER')
    except decouple.UndefinedValueError as e:
        print('Environment Variables not properly set up for Twilio.')
        raise e

    # Send Text Message
    client = Client(account_sid, auth_token)
    message = client.messages.create(to=my_phone_number, from_=twilio_phone_number, body=msg)
    return message.sid


if __name__ == '__main__':
    send_text('testing')
