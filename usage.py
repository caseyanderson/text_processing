# to analyze the Trump Inaugural Address
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import nltk

tags={}
tags['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
tags['adj'] = ['JJ', 'JJR', 'JJS']
tags['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
tags['advrb'] = ['RB', 'RBR', 'RBS']
tags['pronoun'] = ['PRP', 'PRP']


speech = web2soup('http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821')

soup = speech.find_all('p')

html = soup2text(soup)

text = list2string(html, "Chief")

words = tokenizer(text)

soup = nopunc(words)

pos = posTag(soup)

a = tupleSplitter(pos)

filtered = posFilter(a[0], a[1], 'adj', tags)
