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

# to analyze the Trump 2017 Inaugural Address
speech = web2soup('http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821')
soup = speech.find_all('p')
text = soup2text(soup)
text = list2string(text, "Chief")

# to analyze the Obama 2013 Inaugural Address
speech = web2soup('https://www.washingtonpost.com/news/wonk/wp/2013/01/21/transcript-president-obama-2013-inaugural-address/?utm_term=.93826e4af3c8')
soup = speech.find_all('article')
text = soup2text(soup)
text = list2string(text, "Vice President")

# to analyze the Obama 2009 Inaugural Address
speech = web2soup('http://www.nytimes.com/2009/01/20/us/politics/20text-obama.html')
soup = speech.find_all("p", class_="story-body-text story-content")
text = soup2text(soup)
# get rid of applause
text = list2string(text, "whatever")

### back to general below

words = tokenizer(text)

soup = nopunc(words)

pos = posTag(soup)

a = tupleSplitter(pos)

filtered = posFilter(a[0], a[1], 'pronoun', tags)
