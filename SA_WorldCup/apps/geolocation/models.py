from django.db import models

from SA_WorldCup.apps.tweets.models import Tweet

class geolocation(models.Model):
    place = models.TextField(null=True)
    geo = models.TextField(null=True)
    coordinates = models.TextField(null=True)
    
class geolocation_relation(models.Model):
    tweet = models.ForeignKey(Tweet)
    geolocation = models.ForeignKey(geolocation)
