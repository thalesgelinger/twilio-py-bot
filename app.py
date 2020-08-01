from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1> Hello i am a whatsapp bot made by Thales Gelinger </h1>'

@app.route('/bot', methods=['POST'])
def bot():
    resp = MessagingResponse()
    msg = resp.message()
    msg.body('oi')
    return str(resp)


if __name__ == '__main__':
    app.run()