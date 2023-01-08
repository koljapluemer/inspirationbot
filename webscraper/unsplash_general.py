from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

topics = ['hand', 'animal', 'foot', 'portrait', 'landscape']

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)


for topic in topics:

    webdriver.get(f'https://unsplash.com/s/photos/{topic}')
    sleep(1)
    try:
        # find button with content Load more photos
        load_more = webdriver.find_element(By.XPATH, '//button[text()="Load more photos"]')
        # click on button
        load_more.click()
    except: 
        print("No button 'load more photos' found")

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

    with open(f'../global/data/unsplash_{topic}.txt', 'w') as f:
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
                        print(href)
                        # write src and href to txt
                        f.write(href)
                        f.write('\n')
                except:
                    print('trouble extracting data')

webdriver.close()