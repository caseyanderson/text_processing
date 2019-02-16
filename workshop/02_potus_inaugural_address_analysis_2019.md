## POTUS Inaugural Address Analysis
Casey Anderson, Spring 2019

Obama 2013 Inaugural Address (via Washington Post) [here](https://www.washingtonpost.com/news/wonk/wp/2013/01/21/transcript-president-obama-2013-inaugural-address/?noredirect=on&utm_term=.215480df3a09).


### Getting the text (Finding a Corpus)

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

link = 'https://www.washingtonpost.com/news/wonk/wp/2013/01/21/transcript-president-obama-2013-inaugural-address/?noredirect=on&utm_term=.215480df3a09'

url = urlopen(link)

soup = BeautifulSoup(url, 'html.parser')
```

The code above stores all of the text at that url in the `soup` variable.


### Looking at the soup results (Exploring the Corpus)

Executing `soup` in `jupyter notebook`.

This returns all of the text from that URL **including** the speech, the `HTML` formatting the speech and the article around it, any `Javascript` or other scripts that are executed, etc.. Since the goal is to simply get the Inaugural Address one can ignore anything that is not text from the article.

Nonetheless, it's not always easy to locate the portion of the text one cares about, so one often has to scan through the results of `soup` "by hand."

It's also harder to read `HTML` without proper indentation and lineation. `BeautifulSoup` has a method to assist with this known as `prettify`. Execute `print(soup.prettify())` in the terminal to see a prettier version of the page contents.

Easier to read, but still includes lots of stuff that is [noise](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) in this context.

Scan through the the results in the terminal and try to figure out where the article starts and ends. While doing so note any patterns in the construction of the HTML. If it is too hard to find the desired content in the terminal, try using something like Firefox's `Page Source`.


### Removing everything but the article (Conditioning/Cleaning/Filtering the Corpus)

`soup = soup.find_all('p')`

Executing the above line will only return content associated with the tag `p`, a tag which is exclusively used in the speech transcript.

Next check the datatype of the contents of `soup` by executing `type(soup)` in the terminal. This results in `bs4.element.ResultSet`, a datatype that is unique to BeautifulSoup. There are three approaches to figuring out how to handle this data:

1. read the [docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
2. [duckduckgo](https://duckduckgo.com/) the datatype in hopes of finding more information.
3. guess

TBH I started by guessing and happened to guess correctly: one can treat `soup` like a `list` (it vaguely resembled a list in the terminal so this seemed like a logical guess). When filtering a list in Python one typically uses a `for` loop to iterate (do something for every `item`) through a `collection` (a `list` of `items`). Some people think of this as "stepping" through a list.

To test if `soup` may be treated like a `list`, execute the code below in the terminal. One can copy multiple lines of text to the clipboard and paste into the terminal, **while preserving whitespace (!!!)**, by executing `paste` in iPython (this is a feature that is unique to iPython and will not work in many other shells):

```python
counter = 0

for i in soup:
  print('ITEM NO. ' + str(counter) + '\n')
  print(i)
  print('\n')
  counter+=1
```

This confirms that the results of `soup` can be treated like a `list` so we can move on.

Next I am going to use a BeautifulSoup function to grab **only** the text associated with the `p` tags:

```python
text = []

for i in soup:
    text.append(i.text)
```

Printing `text` (`print(text)`) shows the results.

Looks okay but there is some weird noise showing up in certain lines: `\xa0`. Not sure what that is, but it should be removed.

In order to remove `\xa0` we first need to be able to reliably identify it in `text`. Currently `text[2]` returns a line containing `\xa0`. Let's begin by confirming that we can identify that series of characters if it is in a list item:

```python
if '\xa0' in text[2]:
    print('YES')
```

The above `if` statement returns `YES`, confirming that we can identify that character if it is present in our list. Next, we want to remove every instance of '\xa0' if it is in a list item. There are lots of ways to do this, but here is one:

```python
filtered = []
counter = 0

for i in text:
    if '\xa0' in i:
        i = i.replace('\xa0', '')
        filtered.append(i)
    else:
        filtered.append(i)
    print(i)
    counter += 1
```

Printing `filtered` (`print(filtered)`) now shows our cleaned corpus.

The first word Obama actually speaks is "Vice," so we should be able to use the `Python` method `split()` to cut our corpus at that word and remove everything before it. Since `split()` is a method of the `str` (`String`) object one will first have to `join()` the contents of the list into one long string. Run the following code line-by-line to do so:

```python
allofspeech = ''.join(filtered) # converts list items to one long string
allofspeech.find('Vice')
justspeech = allofspeech[26:]
```

Now one can print the entire speech by executing `print(justspeech)` in the terminal.


### Simple Analysis

Length of Speech (characters, includes punctuation and spaces): `len(justspeech)` -> returns 8357

Tokenize by word (includes punctuation, drops whitespace): `tokenized = nltk.word_tokenize(justspeech)`

Removing punctuation to only look at words:

```python
import re

corpus = []
step = 0

for i in tokenized:
    print('position ' + str(step))
    if re.search('[^A-Za-z0-9]+', i) is not None:
        print(str(i) + ' is a symbol, skip!')
    else:
        print(str(i) + ' is not a symbol, keep!')
        corpus.append(str(i))
    step+=1
```

Checking length of corpus now that symbols have been removed: `len(corpus)` -> returns 2055 (number of words)


### Word Frequency

```python
import nltk

freak = nltk.FreqDist(corpus)
freak.most_common(40) # shows the forty most common words ordered by frequency
```

Running `freak.most_common(1)` currently returns `'and', 72`. If one wanted to exclude certain words (like "and") from the corpus, one could analyze the parts of speech of each word and then eliminate all articles and conjunctions, for example.

```python
words = nltk.pos_tag(corpus)
```

The parts of speech tagger outputs a `tuple`, an immutable (un-changeable) datatype that resembles a `list`. It's a lot easier to deal with `lists` in Python than `tuples` (just trust me on this) so the first step is to split the `tuple` into two `lists`:

```python
a,b = zip(*words) # this line is cool, found it while poking around stackoverflow
a = list(a) # btw, you DO have to list caste a otherwise its still a tuple...
b = list(b)
```

To print only the words: `print(a)`, to print only the parts of speech: `print(b)`. As long as the two lists are kept in sync, one list (`b`, parts of speech) can be used to filter another (`a`, words).

Below is a function called `posFilter`. It takes in the two lists created above (list of all words and list of parts of speech) and uses `b` to keep words that belong to parts of speech we care about by passing those words into a new list.

`posFilter` knows which part of speech we care about by looking at the `pos` parameter. This parameter uses the string at `pos` to identify and retrieve the parts of speech tags we want to use from a dictionary (`dct`). Through multiple passes through the original corpus, one is able to prevent `articles`, for example, from appearing in the new list.

```python
def posFilter(corpus, tagged, pos, dct ):
    step = 0
    size = len(tagged)
    posCorpus = corpus
    x = dct[str(pos)]

    for i in x:
        step = 0
        for j in tagged:
            if i == j:
                posCorpus[step] = corpus[step]
                step = step + 1
            else:
                step = step + 1
    return posCorpus
```

Dictionaries (or `dict` for short) in `Python` are similar to `lists` but are comprised of `key` / `value` pairs. `keys` are like labels: they are strings (`str`) used to organize `values` associated with them. the `values` can be anything: an `int`, a `str`, a `list`, another `dict`, etc..

A dictionary is needed here so one can pass a part of speech into the `dict` without needing to know how many tags are associated with that part of speech ahead of time (**yay!**). This is important because there are, for example, four possible tags for `nouns` but only 3 for `adverbs`.

```python
dctnry={}
dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']
dctnry['pronoun'] = ['PRP', 'PRP']
```


### Testing the Filter

```python

dctnry={}
dctnry['noun'] = [ 'NN', 'NNP', 'NNPS', 'NNS']
dctnry['adj'] = ['JJ', 'JJR', 'JJS']
dctnry['vrb'] = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
dctnry['advrb'] = ['RB', 'RBR', 'RBS']
dctnry['pronoun'] = ['PRP', 'PRP']

def posFilter(corpus, tagged, pos, dct ):
    step = 0
    size = len(tagged)
    posCorpus = []
    x = dct[str(pos)]

    for i in x:
        step = 0
        for j in tagged:
            if i == j:
                posCorpus.append(corpus[step])
                step = step + 1
            else:
                step = step + 1
    return posCorpus

filtered = posFilter(a, b, 'noun', dctnry)

```

Now one can run the parts of speech tagger again for a more fine-grained look at word frequency:

```python
import nltk

freak = nltk.FreqDist(filtered)
freak.most_common(25) # shows the fifteen most common words ordered by frequency
```
