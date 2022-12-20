import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm


options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)

url = "https://freesound.org/search/?q=&f=duration%3A%5B0+TO+*%5D&w=&s=Rating+%28highest+first%29&advanced=1&g=1"
webdriver.get(url)

with open('data/freesound.txt', 'w') as f:
    # do 20 times
    for i in range(50):
        # find all a.title elements
        links = webdriver.find_elements(By.CSS_SELECTOR, 'a.title')
        # for every link, save the href attribute
        for link in links:
            f.write(link.get_attribute('href'))
            f.write('\n')
        
        # click on the next button (a tag with content "next")
        sleep(3)
        webdriver.find_element(By.LINK_TEXT, 'next').click()