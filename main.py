from flask import Flask, request
from twilio.rest import Client
import os

app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def receive_sms():
    message_body = request.form['Body']
    from_number = request.form['From']

    # Process the incoming message here
    response_message = 'You said: ' + message_body

    # Send a response message back to the sender
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    message = client.messages.create(
        body=response_message,
        from_=os.environ['TWILIO_PHONE_NUMBER'],
        to=from_number
    )

    return '', 200


if __name__ == '__main__':
    app.run(debug=True)
