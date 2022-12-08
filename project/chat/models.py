from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

User = get_user_model()

class Chat(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

class Message(models.Model):
    sender = models.CharField(max_length=255)
    chat = models.CharField(max_length=255)
    send_at = models.DateTimeField(default= datetime.now, blank=False)
    text = models.CharField(max_length=500)
    class Meta:
        ordering = ('send_at',)