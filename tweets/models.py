# Created by Rubens Pessoa.
# 07/10/2014

from django.db import models

class Tweet(models.Model):
    tweet = models.TextField()

    def __unicode__(self):
        return self.tweet
    
class Tweet_Parsed(models.Model):
    tweet_parsed = models.TextField()

    def __unicode__(self):
        return self.tweet_parsed
    
class Score(models.Model):
    score = models.IntegerField()

    def __unicode__(self):
        return self.score