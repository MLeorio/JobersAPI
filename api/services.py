from twilio.rest import Client
import random

import vonage


def generate_otp():
    code = str(random.randint(100000, 999999))
    return f"{code[:3]}-{code[3:]}"


def send_otp(number, otp):
    account_sid = "your_twilio_account_id"
    auth_token = "your_twilio_auth_token"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Votre code de vérification est {otp}",
        from_="+123456789",  # Numero Twilio
        to=number,
    )
    return message.sid


def send_otp_vonage(number, otp):
    client = vonage.Client(key="31903487", secret="ydxXmwW2cMjXGWRk")
    sms = vonage.Sms(client)

    responseData = sms.send_message(
        {
            "from": "Jobers Artisans",
            "to": str(number),
            "text": f"Votre code de vérification est {otp}",
        }
    )
    
    if responseData["messages"][0]["status"] == "0":
        return("Message envoyé avec succès")
    else:
        return(f"Message failed with error: {responseData['messages'][0]['error-text']}")
