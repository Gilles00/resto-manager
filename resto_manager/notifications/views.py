from django.shortcuts import render
from django.core.mail import EmailMessage
from twilio.rest import TwilioRestClient

def notify(request):
    return render(request, 'notification.html')

def send_email(request):
    email = EmailMessage('Hello', 'World', to=['etsrestomanager@gmail.com'])
    email.send()

    return render(request, 'index.html')

def sms(request):
    
	# Your Account Sid and Auth Token from twilio.com/user/account
	TWILIO_ACCOUNT_SID = 'AC50f3d1912a72cd316697a0e4482b69bd'
	TWILIO_AUTH_TOKEN = 'd65099e18390a7398b7878ea262d5108'

	client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
	
	message = client.messages.create(
		body="U w0t m8",
	    to="+15148278498",
	    from_="+15817014426")

	return render(request, 'index.html')