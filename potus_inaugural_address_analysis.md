## POTUS Inaugural Address Analysis
Casey Anderson, Spring 2017

Trump 2017 Inaugural Address (via ABC News) [here](http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821).

Obama 2013 Inaugural Address (via WhiteHouse.gov) [here](https://obamawhitehouse.archives.gov/the-press-office/2013/01/21/inaugural-address-president-barack-obama).

Obama 2009 Inaugural Address (via NY Times) [here](http://www.nytimes.com/2009/01/20/us/politics/20text-obama.html)


### Getting the text (Finding a Corpus)

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

link = 'http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821'

url = urlopen(link)

soup = BeautifulSoup(url, 'html.parser')
```

The code above stores all of the text at that url in the `soup` variable.


### Looking at the soup results (Exploring the Corpus)

Executing `soup` in `iPython` will return this:

![](/imgs/ugly.png)

This is all of the text from that URL **including** the speech, the `HTML` formatting the speech and the article around it, any `Javascript` or other scripts that are executed, etc.. Since the goal is to simply get the Inaugural Address one can ignore anything that is not text from the article.

Nonetheless, it's not always easy to locate the portion of the text one cares about, so one often has to scan through the results of `soup` "by hand."

It's also harder to read `HTML` without proper indentation and lineation. `BeautifulSoup` has a method to assist with this known as `prettify`. Execute `print(soup.prettify())` in the terminal to see a prettier version of the page contents. For example:

![](/imgs/pretty.png)

Easier to read, but still includes lots of stuff that is [noise](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) in this context.

Scan through the the results in the terminal and try to figure out where the article starts and ends. While doing so note any patterns in the construction of the HTML. If it is too hard to find the desired content in the terminal, try using something like Firefox's `Page Source`.


### Removing everything but the article (Conditioning/Cleaning/Filtering the Corpus)

`soup = soup.find_all('p')`

Executing the above line will only return content associated with the tag `p`. In this case, the terminal returns:

![](/imgs/find_all_p_tag.png)

which is the speech (still including `HTML`). Scrolling up and down through the results confirms that this is the entire text from the URL.

![](/imgs/top_of_article.png)

The article starts with a brief introduction ( "After Donald Trump was sworn in as president...") and a handful of empty `p` tags (no idea why but that is not important right now).

Next check the datatype of the contents of `soup` by executing `type(soup)` in the terminal. This results in `bs4.element.ResultSet`, a datatype that must be unique to BeautifulSoup (this is an educated guess, as I had never heard of such a datatype prior to using BeautifulSoup). There are three approaches to figuring out how to handle this data:

1. read the manual
2. [duckduckgo](https://duckduckgo.com/) the result in hopes of finding more information.
3. guess

TBH I started by guessing and happened to guess correctly: one can treat `soup` like a `list` (it vaguely resembled a list in the terminal so this seemed like a logical test). When filtering a list in Python one typically uses a `for` loop to iterate through a collection. While iterating through a collection one can transform data from an input list and write the results into a new output list, for example.

To test if soup may be treated like a list, execute the code below in the terminal. Note: one can copy multiple lines of text to the clipboard and paste into the terminal, **while preserving whitespace (!!!)**, by executing `paste` in iPython (note: this is a feature that is unique to iPython and will not work in many other shells):

```python
counter = 0

for i in soup:
  print('ITEM NO. ' + str(counter) + '\n')
  print(i)
  print('\n')
  counter+=1
```

Results in something like this in the terminal:

![](/imgs/list_test.png)

This confirms that the results of `soup` can be treated like a `list` so we can move on.

Next I am going to use a BeautifulSoup function to grab **only** the text associated with the `p` tags:

```python
text = []

for i in soup:
    text.append(i.text)
```

Printing `text` (`print(text)`) shows the results:

![](/imgs/results_whitespace_problem.png)

Looks okay but the newline tags are getting rendered as `\n`. In order to get rid of the newline garbage make the following alteration and try again:

```python
text = []

for i in soup:
    text.append(i.text.strip())
```

Printing `text` (`print(text)`) now shows our newline-less corpus:

![](/imgs/no_newlines.png)

The first word Trump actually speaks is "Chief," so we should be able to use the `Python` method `split()` to cut our corpus at that word and remove everything before it. Since `split()` is a method of the `str` (`String`) object one will first have to `join()` the contents of the list into one long string. Run the following code line-by-line to do so:

```python
allofspeech = ''.join(text) # converts list items to one long string
allofspeech.find('Chief')
justspeech = allofspeech[456:]
```

Now one can print the entire speech by executing `print(justspeech)` in the terminal.


### Simple Analysis

Length of Speech (characters, includes punctuation and spaces): `len(justspeech)` -> returns 8357

Tokenize by word (includes punctuation, drops whitespace): `tokenized = nltk.word_tokenize(justspeech)`

Removing punctuation to only look at words:

```python
import re

corpus = []

for i in tokenized:
  if re.search('[^A-Za-z0-9]+', i) is not None:
    print('no match')
  else:
    corpus.append(str(i))
```

Checking length of corpus now that symbols have been removed: `len(corpus)` -> returns 1418 (number of words in the speech)

To figure out the most frequently used words:

```python
import nltk

freak = nltk.FreqDist(output)
freak.most_common(40) # shows the forty most common words ordered by frequency
```
Which results in something like the below:

![](/imgs/most_common.png)


for obama 2013: soup.find_all("div", class_="field-items")
for obama 2009: soup.find_all("p", class_="story-body-text story-content")