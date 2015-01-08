from django.db import models
from SA_WorldCup.apps.tweets.models import Tweet  

class sa_technique(models.Model):
    label = models.TextField(max_length=30)
    description = models.TextField(max_length=140)
    
class sentiment(models.Model):
    tweet = models.ForeignKey(Tweet)
    sentiment = models.IntegerField()
    sentiment_analysis_technique = models.ForeignKey(sa_technique)
    