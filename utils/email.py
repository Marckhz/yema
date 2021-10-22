from django.core.mail import send_mail as django_email

from appointments.dto import EmailDTO



def send_email(email:dict):
    django_email(**email)
