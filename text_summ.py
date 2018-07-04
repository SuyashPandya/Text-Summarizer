# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 10:25:37 2018

@author: Suyash
"""

#import math
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
#from nltk.tokenize import word_tokenize, sent_tokenize
ps = PorterStemmer()
from nltk.stem import WordNetLemmatizer
lm = WordNetLemmatizer()


f = open("AI.txt", 'r')
f1 = f.read()
text = f1.split()
#print(f1)
#print(text)
n=0
freqTable = {}
stop_words = set(stopwords.words('english'))
stop_words.add("?")
stop_words.add("'")
stop_words.add('"')
for word in text:
    word = word.lower()
    word = lm.lemmatize(word)
    word = ps.stem(word)
    if word in stop_words:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1
       
#print(freqTable)
para = f1.split("\n")
senValue = {}

k = 0
summary = []
ind = []
sentences = f1.split(".")
#print(sentences)

for sentence in sentences:
    n += 1
    sen = sentence.split()
    k += 1
    # print(len(sen))
    #key = "key"+str(j)
    
    for i in range(0, len(sen)-1):
        w = sen[i]
        w = w.lower()
        w = lm.lemmatize(w)
        w = ps.stem(w)
        #print(w)
        if sen[i] in stop_words:
            continue
        else:
            #print(freqTable[w])
            if w in freqTable:
                if k in senValue:
                    senValue[k] += freqTable[w]
                else:
                    senValue[k] = freqTable[w]
#print(senValue[key0])      
#print(sentences)
sum=0
for x,v in senValue.items():
    sum += v
#print(sum)
th = sum/n
th=1.2*th
#print(senValue)
#print(th)
newdoc = f1.split(".")
#print(newdoc)

for x,v in senValue.items():
    if v >= th:
        summary.append(newdoc[x-1])
        #print(newdoc[x-1])

#print(summary)     
for output in summary:
    print(output)
