import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)

webdriver.get('https://www.nikonsmallworld.com/galleries/2022-photomicrography-competition/embryonic-hand-of-a-madagascar-giant-day-gecko')

with open('data/nikon.txt', 'w') as f:
    # do 90 times
    for i in range(90):
        # wait until element with class .showiframe is visible
        frame = webdriver.find_element(By.CSS_SELECTOR, '.showiframe')
        # get image 
        image = frame.find_element(By.TAG_NAME, 'img')
        # write image url to txt
        f.write(image.get_attribute('src'))
        f.write('\n')
        # click on the next button
        webdriver.find_element(By.CSS_SELECTOR, '.next').click()
        # wait
        sleep(1)