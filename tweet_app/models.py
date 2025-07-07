from django.db import models

class Tweet(models.Model):
    username = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.username