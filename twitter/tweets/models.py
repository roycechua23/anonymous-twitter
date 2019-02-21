from django.db import models
from datetime import datetime

# Create your models here.
class Tweets(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=1000)
    date_posted = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title
