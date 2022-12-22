import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
import random

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)

webdriver.get('https://film-grab.com/movies-a-z/')

# find a.title
# get href

links = webdriver.find_elements(By.CSS_SELECTOR, 'a.title')
# select 100 random links
links = random.sample(links, 100)
hrefs = [link.get_attribute('href') for link in links]

with open('../global/data/movies.txt', 'w') as f:
    for href in hrefs:
        webdriver.get(href)
        # get .bwg_lightbox" 
        images = webdriver.find_elements(By.CSS_SELECTOR, '.bwg_lightbox')
        # get first 10 links
        image_links = [image.get_attribute('href') for image in images[:10]]
        for l in image_links:
            f.write(l + ' ' + href)
            f.write('\n')
        sleep(3)


        