from django.conf import settings
from twilio.rest import Client


class MessageHandler:
    phone_number = None
    otp = None

    def __init__(self, phone_number, otp) -> None:
        self.phone_number = phone_number
        self.otp = otp

    def send_otp_via_message(self):
        client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
        # message = client.messages.create(
        #     body=f"your otp is:{self.otp}",
        #     from_=f"{settings.TWILIO_PHONE_NUMBER}",
        #     to=f"{settings.COUNTRY_CODE}{self.phone_number}",
        # )
        account_sid = "AC3ceb6e927d80bf005df15d6ddae99797"
        auth_token = "969035faab28ac9dccda7459ee63319d"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Your otp  {self.otp}",
            from_="+16205019659",
            to="+917989508993",
        )
        print(message.sid)

    # def send_otp_via_whatsapp(self):
    #     client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)
    #     message = client.messages.create(
    #         body=f"your otp is:{self.otp}",
    #         from_=f"{settings.TWILIO_WHATSAPP_NUMBER}",
    #         to=f"whatsapp:{settings.COUNTRY_CODE}{self.phone_number}",
    #     )
