from lib2to3.pgen2 import token
from django.db import models
from django.contrib.auth.models import User
import uuid


# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    token = models.CharField(default='', max_length=1000)
    is_verified = models.BooleanField(default=False)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def save(self ,*args , **kwargs):
        self.token = str(uuid.uuid4())
        super(Profile , self).save(*args , **kwargs)
