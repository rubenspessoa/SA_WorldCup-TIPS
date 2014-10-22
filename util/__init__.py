# coding: utf-8
# Created by Rubens Pessoa.
# 07/10/2014

from tweets.models import Tweet

def pre_process(text):
    from nltk.corpus import stopwords
    import string
    final_answer = []
    
    # TIRA STOPWORDS
    stop = stopwords.words("english")
    text = [word for word in text.split() if word not in stop]
    
    # TIRA SUBTRINGS 
    text = [i for i in text if not contain_substring(i)]
    
    # TIRA PONTUACAO
    unsafechars = string.punctuation + "0123456789"
       
    for word in text:
        new_word = ''.join(char for char in word if char not in unsafechars)
        final_answer.append(new_word)
    
    blank = ''
    blank_spaces = [" ", blank]
    
    final_answer = [word for word in final_answer if word not in blank_spaces]
    return final_answer
    

def contain_substring(word):
    substrings = ["http","RT","@", "#"]    
    flag = False
    for substring in substrings:
        if word.find(substring) != -1:
            flag = True
    return flag 

    
def stringToDict(text):
    import ast
    return ast.literal_eval(text)      
    
def tweets_count():
    all_entries = Tweet.objects.all()[1427:1435]
    contador = 0
    
    for entry in all_entries:
        tweet = entry.tweet
        tweet_dict = ast.literal_eval(tweet)
        print tweet_dict['text'].split()
        if "#WorldCup" in tweet_dict['text'].split():
            contador += 1
            
    print contador
    
