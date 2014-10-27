# -*- coding: utf-8 -*-
#
# A framework of sentiment analysis applied on the tweets related to the 2014 FIFA World Cup.
# Copyright (C) 2014 Rubens Pessoa 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>
#
#

from util import string_to_dict, pre_process, phrase_strength, is_in_english

PATH = '/home/kiko/workspace/Tweets_WorldCup_2014/'

if __name__ == '__main__':
    import sqlite3

    bd1 = sqlite3.connect(PATH + 'db-1.sqlite3')
    bd2 = sqlite3.connect(PATH + 'db-2.sqlite3')
    bd3 = sqlite3.connect(PATH + 'db-3.sqlite3')
    
    bd1_cursor = bd1.cursor()
    
    contador = 0
    for row in bd1_cursor.execute("SELECT tweet FROM tweets_tweet"):
        if contador >= 481265:
            tweet_dict = string_to_dict(row[0])
            if is_in_english(tweet_dict):
                tweet_text = tweet_dict['text']
                pre_processed = pre_process(tweet_text)
                if len(pre_processed) > 0:
                    print phrase_strength(pre_processed), tweet_text 
            contador += 1
        else:
            contador += 1
    print contador

    