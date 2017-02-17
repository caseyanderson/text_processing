

# takes a url as input, outputs a soup object
def web2soup(link):
    url = urlopen(str(link))
    soup = BeautifulSoup(url, 'html.parser')
    return soup


# takes a filtered soup object as input, returns only text content from html, strips newline chars, outputs list
def soup2text(soup):
    text = []

    for i in soup:
        text.append(i.text.strip())
    return text


# takes a list item as input, uses a speech start word to cut out intro (etc.), and outputs one string (justspeech)
def list2string(corpus_list, start_word):
    start = None

    allofspeech = ''.join(corpus_list) # converts list items to one long string
    pos = allofspeech.find(str(start_word))
    start = pos - 1
    justspeech = allofspeech[start: ]
    return justspeech


# takes a string as input, outputs a list of words
def tokenizer(corpus):
    tokenized = nltk.word_tokenize(corpus)
    return tokenized


# takes a list of words as input, returns a new list with no punctuation
def nopunc(tokenized):
    corpus = []
    step = 0

    for i in tokenized:
        print('position ' + str(step))
        if re.search('[^A-Za-z0-9]+', i) is not None:
            print(str(i) + ' is a symbol, skip!')
        else:
            corpus.append(str(i))
        step+=1
    return corpus


# takes a word list as input, returns a new tuple with parts of speech tags
def posTag(corpus):
    words = nltk.pos_tag(corpus)
    return words


# takes a tuple and splits it into two lists
def tupleSplitter(corpus):
    a,b = zip(*corpus)
    a = list(a)
    b = list(b)
    return a, b


# takes corpus, pos tag lists and dictionary of parts of speech tag terms, uses pos to choose tags, outputs parts of speech only
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


# make the stuff lowercase
def lower(filtered):
    counter = 0

    for i in filtered:
        filtered[counter] = i.lower()
        counter +=1
    return filtered


# this will return the error code number
def show_errors(url):
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
        print('success!')
    except urllib.error.URLError as error:
        print("Error no. " + str(error.code))
