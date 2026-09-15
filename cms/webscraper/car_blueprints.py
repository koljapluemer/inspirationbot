import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options


webdriver = webdriver.Firefox()
webdriver.get('https://blueprintbox.com/categories.php?cat_id=22')


links = []

content_row = webdriver.find_element(By.CSS_SELECTOR, '.row')
# get all b tags
b_tags = content_row.find_elements(By.TAG_NAME, 'b')
# for every b tag, get the grandparent 
# if it is an a tag, get the href attribute
for b in b_tags:
    parent = b.find_element(By.XPATH, '..')
    grandparent = parent.find_element(By.XPATH, '..')
    if grandparent.tag_name == 'a':
        links.append(grandparent.get_attribute('href'))

# print(links)

with open ('data/car_blueprints.txt', 'w') as f:
    for link in links:
        print('opening link: ' + link)
        webdriver.get(link)
        # get all img tags
        imgs = webdriver.find_elements(By.TAG_NAME, 'img')
        # for every img tag, get the src attribute
        for img in imgs:
            src = img.get_attribute('src')
            full_size_img = src.replace('thumbnails', 'media')
            # write the full size image url to txt
            f.write(full_size_img)
            f.write('\n')
    sleep(1)
    

