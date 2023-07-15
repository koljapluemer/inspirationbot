import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

links = []

webdriver = webdriver.Firefox(options=options)
with open('../global/data/artvee_realism.txt', 'w') as f:
    # enumerate from 2 to 205
    for i in range(2, 205):
        print(f'Page {i}')
        webdriver.get(f'https://artvee.com/movement/realism/page/{i}/')
        sleep(1)
        # get all elements .product-title
        elements = webdriver.find_elements(By.CSS_SELECTOR, 'h3.product-title')
        for element in elements:
            try:
                # get href of child a
                href = element.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                if not href in links:
                    links.append(href)
                    # print(href)
                    f.write(href + '\n')
            except Exception as e:
                print('Error:', e)