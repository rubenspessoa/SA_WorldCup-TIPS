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

def string_to_dict(text):
    import ast
    return ast.literal_eval(text)
    
def rate_sentiment(sentiString):
    import shlex, subprocess
    
    #open a subprocess using shlex to get the command line string into the correct args list format
    commands = shlex.split("java -jar SentiStrength.jar stdin sentidata /home/kiko/workspace/Sentistrength/")
    p = subprocess.Popen(commands,
                         cwd=r'/home/kiko/workspace/Sentistrength/', 
                         stdin = subprocess.PIPE, 
                         stdout = subprocess.PIPE, 
                         stderr = subprocess.PIPE)
    
    #communicate via stdin the string to be rated. Note that all spaces are replaced with +
    stdout_text, stderr_text = p.communicate(sentiString)
    #remove the tab spacing between the positive and negative ratings. e.g. 1    -5 -> 1-5
    stdout_text = stdout_text.rstrip().replace("\t","")
    
    return count_strength(stdout_text)

def count_strength(strengths):
        positive_strength = 0
        negative_strength = 0
        
        for char in strengths:
            if char in "0123456789":
                if positive_strength == 0:
                    positive_strength = int(char)
                else:
                    negative_strength = int(char)
        
        return positive_strength - negative_strength
    
def phrase_strength(word_list):
    sum_strengths = 0
    for word in word_list:
        sum_strengths += rate_sentiment(word.encode('utf8'))
    return sum_strengths
    
    
    
        
        