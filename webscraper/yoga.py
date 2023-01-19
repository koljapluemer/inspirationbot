from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

# set up webdriver and go to https://www.yogajournal.com/pose-finder/pose-finder/
options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)
webdriver.get('https://www.yogajournal.com/pose-finder/pose-finder/')

sleep(1)

# if there is a #onetrust-accept-btn-handler button, click it
try:
    accept = webdriver.find_element(By.ID, 'onetrust-accept-btn-handler')
    accept.click()
except:
    print('No button to accept cookies found')

sleep(1)

# find table where border="0"
table = webdriver.find_element(By.CSS_SELECTOR, 'table[border="0"]')
# find all rows in table
rows = table.find_elements(By.TAG_NAME, 'tr')
# for every row, get the first child link
for row in rows:
    try:
        link = row.find_elements(By.TAG_NAME, 'a')[0]
        href = link.get_attribute('href')
        with open('../global/data/yoga.txt', 'a') as f:
            f.write(href)
            f.write('\n')
    except:
        print('trouble extracting data from this row')

webdriver.close()