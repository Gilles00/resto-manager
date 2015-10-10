#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.core.mail import EmailMessage
from twilio.rest import TwilioRestClient

class NotificationUtility():
    
    @staticmethod
    def send_email(email, message):
        email = EmailMessage('Changement d\'état de la commande', message, to=[email])
        email.send()
        return True
    
    @staticmethod
    def send_sms(phone_number, message):
        #Your Account Sid and Auth Token from twilio.com/user/account
        TWILIO_ACCOUNT_SID = 'AC50f3d1912a72cd316697a0e4482b69bd'
        TWILIO_AUTH_TOKEN = 'd65099e18390a7398b7878ea262d5108'
        client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=message,
            to='+1' + phone_number,
            from_="+15817014426")
        return True