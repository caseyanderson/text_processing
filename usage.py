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

######### to analyze the Trump 2017 Inaugural Address
speech = web2soup('http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821')
soup = speech.find_all('p')
text = soup2text(soup)
text = list2string(text, "Chief")
#########

######### to analyze the Obama 2013 Inaugural Address
speech = web2soup('https://www.washingtonpost.com/news/wonk/wp/2013/01/21/transcript-president-obama-2013-inaugural-address/?utm_term=.93826e4af3c8')
soup = speech.find_all('article')
text = soup2text(soup)
text = list2string(text, "Vice President")
#########

######### to analyze the Obama 2009 Inaugural Address
speech = web2soup('http://obamawhitehouse.archives.gov/blog/2009/01/21/president-barack-obamas-inaugural-address')
soup = speech.find_all("div", class_="legacy-para")
text = soup2text(soup)
text = list2string(text, "My fellow citizens")
#########

######### back to general below
words = tokenizer(text)
soup = nopunc(words)
pos = posTag(soup)
a = tupleSplitter(pos)

filtered = posFilter(a[0], a[1], 'adj', tags)

# surely these next three lines can be one function
filtered = lower(filtered)
freak = nltk.FreqDist(filtered)

freak.most_common(25) # shows the fifteen most common words ordered by frequency
