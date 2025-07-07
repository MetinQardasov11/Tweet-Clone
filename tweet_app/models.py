from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tweets')
    message = models.TextField()
    
    def __str__(self):
        return self.username