#! python3
# Write a program that, given the URL of a web page, will attempt to download
# every linked page on the page. The program should flag any pages
# that have a 404 “Not Found” status code and print them out as broken links.

''' Ask for a website
    Attempt to download the website
        raise_for_status, exit if unsuccesfull
    Store the contents in a bs4 variable
    Select all <a> tags from the page
    Process the <a> tags
        if it starts with http(s) or www then just attempt to download them
        if it starts with '/' then add site url before '/' and attempt dwnld
            if the status_code is 404 then print it
'''
import requests, bs4, os

flag = True

# 2 things can go wrong, the url can be incorrectly typed (without http(s)://)
# even if it has correct schema, it just can be invalid
while flag:
    # Ask for a website
    webUrl = input("Type the website url: ")
    try:
        # Attempt to download the website
        stContents = requests.get(webUrl)
        flag = False
    except Exception as exc:
        print("An exception happened: %s" % (exc))
        flag = True

# check if the site exists if not terminate the program
try:
    stContents.raise_for_status()
except Exception as exc:
    print("An exception happened: %s"  %(exc))
    quit()

# if we got to this point create a directory
title = os.path.basename(webUrl)
os.makedirs(title, exist_ok=True)

# Store the contents in a bs4 variable
soup = bs4.BeautifulSoup(stContents.text, 'html.parser')

# Select all <a> tags from the page
links = soup.select('a')

# Process the <a> tags
for i in range(len(links)):
    url = links[i].get('href')

    # often the web has links to itself, just omit them
    if(url == webUrl or url == None):
        continue
    #  if it starts with '/' then add site url before '/' and attempt dwnld
    elif(url.startswith('/')):
        url = webUrl + url

    #print("Downloading %s..." %(url))
    # ignores incorrectly schemed links
    try:
        linkCnt = requests.get(url)
    except Exception as exc:
        continue
            
    try: 
        linkCnt.raise_for_status()
    except Exception as exc:
        # print only when 404 error happens
        if linkCnt.status_code == 404:
            print("An exception happened: %s" % (exc))
        continue

    # download only the pages without errors
    '''pageFile = open(title, os.path.basename(url), 'wb')
    for chunk in linkCnt.iter_content(100000):
        pageFile.write(chunk)
    pageFile.close()'''

print("Done.")
