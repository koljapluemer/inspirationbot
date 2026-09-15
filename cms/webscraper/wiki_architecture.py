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
webdriver.get('https://en.wikipedia.org/wiki/List_of_architectural_styles#Chronology_of_styles')

# #mw-content-text
content = webdriver.find_element(By.ID, 'mw-content-text')
# find li
lis = content.find_elements(By.TAG_NAME, 'li')
# get all a within the lis 
links = []
for li in lis:
    links += li.find_elements(By.TAG_NAME, 'a')

hrefs = [link.get_attribute('href') for link in links]
print('Found {} hrefs'.format(len(hrefs)))

with open('../global/data/architecture.txt', 'w') as f:
    for href in hrefs:
        if not '#' in href and '/wiki/' in href and not 'File:' in href:
            print('---- Checking {}'.format(href))
            webdriver.get(href)
            sleep(3)
            try:
                # .infobox-image
                infobox = webdriver.find_element(By.CSS_SELECTOR, '.infobox-image')
                # get first element a.image
                image = infobox.find_element(By.TAG_NAME, 'a')
                href = image.get_attribute('href')
                print('---- Found image {}'.format(image.get_attribute('href')))
                # open image 
                image.click()
                file = webdriver.find_element(By.CLASS_NAME, 'mw-mmv-image')
                print('found file tag', file)
                src = file.find_element(By.TAG_NAME, 'img').get_attribute('src')
                f.write(src + ' ' + href + '\n')

            except Exception as e:
                print('---- error:', e)

        else:
            print('---- Skipping {}'.format(href))

        print('------')