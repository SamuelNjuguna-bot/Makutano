from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
class Background(models.Model):
    image = models.ImageField(upload_to='media/')

class Room(models.Model):
    room = models.CharField(max_length=100000)
class Message(models.Model):
    message = models.CharField(max_length=1000000)
    username = models.CharField(max_length=100000)
   
class UserQueries(models.Model):
    
    SENDER_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )
    
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:20]}..."