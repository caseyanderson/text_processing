## POTUS Inauguration Speech Analysis
Casey Anderson, Spring 2017


A transcript (ABC News) of the Trump Inauguration Speech, used as an example throughout, can be found [here](http://abcnews.go.com/Politics/full-text-president-donald-trumps-inauguration-speech/story?id=44915821).


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

This is all of the text from that URL **including** the speech, the `HTML` formatting the speech and the article around it, any `Javascript` or other scripts that are executed, etc.. Since the goal is to simply get the Inauguration Speech one can ignore anything that is not text from the article.

Nonetheless, it's not always easy to locate the portion of the text one cares about, so one often has to scan through the results of `soup` "by hand."

It's also harder to read `HTML` without proper indentation and lineation. `BeautifulSoup` has a method to assist with this known as `prettify`. Execute `print(soup.prettify())` in the terminal to see a prettier version of the page contents. For example:

![](/imgs/pretty.png)

Easier to read, but still includes lots of stuff that is [noise](https://en.wikipedia.org/wiki/Signal-to-noise_ratio) in this context.

Scan through the the results in the terminal and try to figure out where the article starts and ends. While doing so note any patterns in the construction of the HTML.


### Removing everything but the article (Conditioning/Cleaning/Filtering the Corpus)

`soup = soup.find_all('p')`

Executing the above line will only return content associated with the tag `p`. In this case, the terminal returns:

![](/imgs/find_all_p_tag.png)

which is the speech (still including `HTML`). Scrolling up and down through the results confirms that this is the entire text of the article.

![](/imgs/top_of_article.png)

Scrolling all the way up to the beginning of the article confirms that it starts with a brief introduction ( "After Donald Trump was sworn in as president...") and a handful of empty `p` tags (no idea why but that is not important right now).
