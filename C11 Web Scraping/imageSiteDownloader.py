#! python3
# imageSiteDownloader.py - downloads images from pexels.com
# 

import requests, os, bs4, sys, re

# check argument
if len(sys.argv) > 1:
    url = 'http://www.pexels.com/search/'
    title = ''

    # concatenate the searched keywords
    for i in range(1, len(sys.argv)):
        title += sys.argv[i] + ' '
    url += title

    # download the contents of the site
    print("Downloading page %s" % url)
    res = requests.get(url)
    res.raise_for_status()
    
    # parse the contents with bs4
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # store first 10 tags in a list
    tags = soup.select('img[srcset]', limit=10)

    # get links to these images and store them in the list
    links = []
    for i in range (0, len(tags)):
        links.append(tags[i].get('data-big-src'))
    
    # create regex object and directory for images
    # the directory name is created from searched keywords
    imgRegex = re.compile(r'.*(?=\?)')
    os.makedirs(title, exist_ok=True)

    # loop through the links list and download the images
    for i in range(0, len(links)):
        # format the links using regex
        imgUrl = imgRegex.search(links[i]).group(0)

        # download the image
        print('Downloading image %s...' % (imgUrl))
        res = requests.get(imgUrl)
        res.raise_for_status()

        # save the image to ./'title'.
        imageFile = open(os.path.join(title.rstrip(), os.path.basename(imgUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    print('Done.')
else:
    print("Wrong argument.")
