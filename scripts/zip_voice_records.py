from twilio.rest import Client

import localsettings

def post_template_message():
    client = Client(localsettings.TWILLIO_ACCOUNT_SID, localsettings.TWILLIO_AUTH_TOKEN)
    message = client.messages.create(
        body='Your {{1}} order of {{2}} has shipped and should be delivered on {{3}}. Details : {{4}}',
        from_= localsettings.FROM_NUMBER,
        to= localsettings.TO_NUMBER)
    print(message.sid)

if __name__ == "__main__":
    post_template_message()
