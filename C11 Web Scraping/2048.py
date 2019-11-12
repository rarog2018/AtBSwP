#! python3
# 2048.py - automatically plays https://gabrielecirulli.github.io/2048/ game

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# body tag is reachable for keyboard
bodyTag = browser.find_element_by_tag_name('body')
# paragraph within div that has a class 'game-container'
cssSel = 'div[class = "game-container"] p'
# string with game message
gameMsg = 'Game over!'

# until the text in the paragraph is not 'Game over!' play the game
while (browser.find_element_by_css_selector(cssSel).text) != gameMsg:
    bodyTag.send_keys(Keys.UP)
    bodyTag.send_keys(Keys.RIGHT)
    bodyTag.send_keys(Keys.DOWN)
    bodyTag.send_keys(Keys.LEFT)

print("Done.")
