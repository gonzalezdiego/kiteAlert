from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

TWILIO_SID = "{YOUR_TWILIO_SID}"
TWILIO_TOKEN = "{YOUR_TWILIO_TOKEN}"
TWILIO_FROM_NUMBER = "{YOUR_TWILIO_FROM_NUMBER}"

class NotificacionManager:
    def __init__(self):
        pass

    def send_message(self, message,to_number):
        proxy_client = TwilioHttpClient()
        client = Client(TWILIO_SID, TWILIO_TOKEN, http_client=proxy_client)
        message = client.messages \
                .create(
                body=message,
                from_=TWILIO_FROM_NUMBER,
                to=to_number
                    )

    def format_message(self, date, wind_speed):
        message = f"Prepara el Kite para el {date} en Concepcion del Uruguay. Mas de {wind_speed} nudos. Solta la Barraaa"
        return message

