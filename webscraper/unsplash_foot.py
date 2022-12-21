from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)

webdriver.get('https://unsplash.com/s/photos/foot')
sleep(1)
# find button with content Load more photos
try:
    load_more = webdriver.find_element(By.XPATH, '//button[text()="Load more photos"]')
    # click on button
    load_more.click()
except:
    print('oops no button')

def __scroll_down_page(self, speed=28):
    current_scroll_position, new_height= 0, 1
    while current_scroll_position <= new_height:
        if current_scroll_position > 80000:
            break
        current_scroll_position += speed
        webdriver.execute_script("window.scrollTo(0, {});".format(current_scroll_position))
        new_height = webdriver.execute_script("return document.body.scrollHeight")

__scroll_down_page(webdriver)

# get by class .rEAWd
pictures = webdriver.find_elements(By.CSS_SELECTOR, '.rEAWd')

with open('../global/data/unsplash_foot.txt', 'w') as f:
    for picture in pictures:
        # check if element with content 'Unsplash+' exists
        if not picture.find_elements(By.XPATH, '//span[text()="Unsplash+"]'):
            try:
                # get href of picture
                href = picture.get_attribute('href').split('?')[0]
                # find image within picture
                image = picture.find_element(By.TAG_NAME, 'img')
                # get src of image
                src = image.get_attribute('src').split('?')[0]
                # if not plus in src    
                if not 'plus' in src:
                    print(src, href)
                    # write src and href to txt
                    f.write(src + ' ' + href)
                    f.write('\n')
            except:
                print('trouble extracting data')