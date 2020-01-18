#! python3
# plugin that checks the updates and downloads the comics from the lht.com

import bs4, os, requests

# global variables
lhtUrl = "http://www.lefthandedtoons.com/"
lhtPath = './comicDownloads/lhtComics'

def first_preparation():
    print("Preparing first download from lht...")
    # create a folder for downloaded comics
    os.makedirs(lhtPath, exist_ok=True)
    lastComicNumber = check_last_number()
    return lastComicNumber


def check_last_number():
    print("Checking the last comic on %s..." % lhtUrl)
    # download the contents of lht.com
    res = requests.get(lhtUrl)
    res.raise_for_status()

    # find the number of the comic under the 'prev' button
    lhtSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    # select all anchor element inside elements with class 'prev'
    lhtPrev = lhtSoup.select('.prev a')
    lhtPrev = lhtPrev[0].get('href')
    lhtPrevNum = lhtPrev[1:-1]    # strips from the '/' characters
    return int(lhtPrevNum) + 1


def download_comics(firstComic, lastComic):
    # go through every single page in the given range
    for comicNumber in range(firstComic, lastComic):
        print("Downloading the page %s%s..." % (lhtUrl, str(comicNumber)))
        # download the contents of the page
        res = requests.get(lhtUrl + str(comicNumber))
        res.raise_for_status()

        # find the url of the image
        comicSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem = comicSoup.select('.comicimage')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./comicDownloads/lhtComics
            imageFile = open(os.path.join(
                lhtPath, os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
