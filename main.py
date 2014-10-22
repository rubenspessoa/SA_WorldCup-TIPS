# coding: utf-8
# Created by Rubens Pessoa.
# 07/10/2014

from util import stringToDict, pre_process, contain_substring

PATH = '/home/kiko/workspace/SA_WorldCup/Tweets_WorldCup_2014/'

if __name__ == '__main__':
    import sqlite3

    bd1 = sqlite3.connect(PATH + 'db-1.sqlite3')
    bd2 = sqlite3.connect(PATH + 'db-2.sqlite3')
    bd3 = sqlite3.connect(PATH + 'db-3.sqlite3')
    
    bd1_cursor = bd1.cursor()
    
    contador = 0
    
    for row in bd1_cursor.execute("SELECT tweet FROM tweets_tweet"):
        if contador >= 481265:
            dict_row = stringToDict(row[0])
            if dict_row["lang"] == "en":
                tweet = dict_row['text']
                pre_processed = pre_process(tweet)
                if len(pre_processed) > 0:
                    print pre_processed
        else:
            contador += 1
