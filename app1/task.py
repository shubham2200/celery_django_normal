
# from celery import shared_task
from .models import *
from celery_django.celery import app
import datetime
from django.core.mail import send_mail
from django.conf import *

@app.task(name = "send_notification")
def send_notification():
    try:
        time_thresold = datetime.now() - datetime.timedelta(hours= 2)

        profile_obj = Profile.objects.filter(is_verified = False , create_at__gte = time_thresold)
        
        for profile_obj in profile_obj:
            subject = "notification you account has not veri"
            message = 'your account has not verif'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [profile_obj.email]
            send_mail(subject , message , email_from  , recipient_list)



    except Exception as e:
        print(e)


















# @shared_task
# def sleepy(duration):
#     sleep(duration)
#     return None