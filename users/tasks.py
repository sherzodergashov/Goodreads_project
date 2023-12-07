from django.core.mail import send_mail
from config.celery import app

@app.task()
def send_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        "sherzod.ergashov.4501@gmail.com",
        recipient_list
    )
