# Created by Rubens Pessoa.
# 07/10/2014

path = '/home/kiko/workspace/SA_WorldCup/Tweets_WorldCup_2014/'

from tweets.models import Tweet

import sqlite3, ast

def conexao_teste():
    bd1 = sqlite3.connect(path + 'db-1.sqlite3')
    bd2 = sqlite3.connect(path + 'db-2.sqlite3')
    bd3 = sqlite3.connect(path + 'db-3.sqlite3')
    
    
def tweets_count():
    all_entries = Tweet.objects.all()[1427:]
    contador = 0
    
    for entry in all_entries:
        tweet = entry.tweet
        tweet_dict = ast.literal_eval(tweet)
        print tweet_dict['text'].split()
        if "#WorldCup" in tweet_dict['text'].split():
            contador += 1
            
    print contador
    
