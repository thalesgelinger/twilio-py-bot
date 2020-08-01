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

    incomming_msg = request.values.get('Body', '').lower()
    
    if 'cachorro' in incomming_msg:
        response = requests.get('https://dog.ceo/api/breeds/image/random').json()
        dog_image = response["message"]
        msg.media(dog_image)
    else:
        msg.body('Num entendi foi nada, ASUHDUASHDUAHSDUHASUD')

    return str(resp)


if __name__ == '__main__':
    app.run()