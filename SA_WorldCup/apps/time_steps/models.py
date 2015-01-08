from django.db import models
from SA_WorldCup.apps.tweets.models import Tweet

class time_steps(models.Model):
    description = models.TextField(max_length=140)
    
class timing(models.Model):
    tweet = models.ForeignKey(Tweet)
    timing = models.TextField(null=True)
    time_step = models.ForeignKey(time_steps)

    
