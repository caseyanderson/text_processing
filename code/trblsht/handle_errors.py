# working on error handling

# this nytimes article returns a 303 error, this concept gives a way
url ='https://www.nytimes.com/2017/02/16/us/politics/donald-trump-press-conference-transcript.html'

# this will return the error code number
def handle_errors(url):
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
        print('success!')
    except urllib.error.URLError as error:
        print("Error no. " + str(error.code))
