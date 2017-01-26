
# simple stuff ->
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')


# extract all urls in <a> tags:
for link in soup.find_all('a'):
    print(link.get('href'))


# print all text
print(soup.get_text())




## analyzing the inauguration speech

from bs4 import BeautifulSoup
from urllib.request import urlopen

url = urlopen('http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821')

soup = BeautifulSoup(url,'html.parser')

# check to see pretty version of html
print(soup.prettify())

# often times have to read through the html to see how to identify what you are looking for...

# example img
# here i see lots of code but not the full text of the inauguration speech, which is what i want
