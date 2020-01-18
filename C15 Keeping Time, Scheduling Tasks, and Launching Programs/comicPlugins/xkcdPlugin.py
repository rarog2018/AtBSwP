#! python3
# plugin that checks the updates and downloads the comics from the xkcd.com

import bs4, os, requests

# global variable
xkcdUrl = "http://xkcd.com/"
xkcdPath = './comicDownloads/xkcdComics'

def first_preparation():
    print("Preparing first download from xkcd...")
    # create a folder for downloaded comics
    os.makedirs(xkcdPath, exist_ok=True)
    lastComicNumber = check_last_number()
    return lastComicNumber


def check_last_number():
    print("Checking the last comic on http://xkcd.com...")
    # download the contents of xkcd.com
    res = requests.get(xkcdUrl)
    res.raise_for_status()

    # find the number of the comic under the 'prev' button
    xkcdSoup = bs4.BeautifulSoup(res.text, 'html.parser')
    xkcdPrev = xkcdSoup.select('a[rel="prev"]')
    xkcdPrev = xkcdPrev[0].get('href')
    xkcdPrevNum = xkcdPrev[1:-1]    # strips from the '/' characters
    return int(xkcdPrevNum) + 1

def download_comics(firstComic, lastComic):
    # go through every single page in the given range
    for comicNumber in range(firstComic, lastComic):
        print("Downloading the page %s%s..." % (xkcdUrl, str(comicNumber)))
        # download the contents of the page
        res = requests.get(xkcdUrl + str(comicNumber))
        res.raise_for_status()

        # find the url of the image
        comicSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        comicElem = comicSoup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = 'http:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image %s...' % (comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()

            # Save the image to ./comicDownloads/xkcdComics
            imageFile = open(os.path.join(
                xkcdPath, os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()


