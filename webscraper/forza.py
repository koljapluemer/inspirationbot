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
webdriver.get('https://forza.fandom.com/wiki/Forza_Horizon_4/Cars')

sleep(1)
# find div with content 'ACCEPT' and click
webdriver.find_element(By.XPATH, '//div[text()="ACCEPT"]').click()

sleep(1)

# find table with class jquery-tablesorter
table = webdriver.find_element(By.CSS_SELECTOR, '.jquery-tablesorter')
table_body = table.find_element(By.TAG_NAME, 'tbody')
# find all links within     
links = table_body.find_elements(By.TAG_NAME, 'a')

urls = []

for link in links:
    url = link.get_attribute('href')
    if 'https://forza.fandom.com' in url:
        urls.append(url)



with open('../global/data/forza.txt', 'w') as f:
    # get the images from the car profiles 
    for url in urls: 
        try: 
            print(f'---- Checking {url}')
            webdriver.get(url)
            # get a tag with class image-thumbnail
            a = webdriver.find_element(By.CSS_SELECTOR, '.image-thumbnail')
            href = a.get_attribute('href')
            print(f'---- Found {href}')
            # write image url to txt
            f.write(href + ' ' + url)
            # newline
            f.write('\n')
            sleep(1)
        except:
            print(f'---- Error on {url}')
            sleep(1)

# close the browser
webdriver.quit()

# TODO: the images are mostly thumbnail sized, why?