## text processing pre-flight

Below are instructions regarding installing things needed to participate in this workshop. They include:

* Xcode (just for the Command Line Tools)
* Homebrew
* Python3
* iPython3
* BeautifulSoup4
* Natural Language Toolkit

### Xcode / The Command Line Tools

Do you have Xcode on your computer? To check to see if you have Xcode on your CPU, go to the terminal and type the following:

`xcode-select -p`

If you see this as a response:

`/Applications/Xcode.app/Contents/Developer`

Then you have Xcode and can proceed to the next step.

If you do **not** see this as a response:

`/Applications/Xcode.app/Contents/Developer`

Then you do **not** have `Xcode` and need to download it from [here](https://itunes.apple.com/us/app/xcode/id497799835?mt=12).

Once you have downloaded `Xcode`, go back to your terminal and enter this command:

`xcode-select --install`

Which should bring up something like this:

![](imgs/xcode-select_install_cmnd_line_tools.png)

Click `Install` to download and install the `Xcode Command Line Tools` (it takes a while so maybe go make some food or get a cup of coffee or something).

### homebrew

Copy and paste this code into the terminal and press `enter` to install [homebrew](http://brew.sh/):  `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

If prompted, agree to the Xcode license:

![](imgs/agree_to_xcode_license.png)

By running `sudo xcodebuild -license` in the terminal.

### python3

`brew search python3`

`brew install python3`

python package manager pip comes with python...

`pip3 search ipython`

`pip3 install ipython`

`ipython3` runs the ide

install beautiful soup

pip3 install beautifulsoup4

install nltk
pip3 search nltk

results (screenshot)

`sudo pip3 install -U nltk`

confirm that it works:

ipython3
import nltk
nltk. and then hit you tab key

getting nltk things

ipython3
import nltk
nltk.download()

see photos
