# -*- coding: utf-8 -*-
#
# A framework of sentiment analysis applied on the tweets related to the 2014 FIFA World Cup.
# Copyright (C) 2014 Rubens Pessoa 
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
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
    
