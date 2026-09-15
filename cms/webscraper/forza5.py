import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)
webdriver.get('https://forza.fandom.com/wiki/Category:Cars_(FH5)')

sleep(1)
# find div with content 'ACCEPT' and click
webdriver.find_element(By.XPATH, '//div[text()="ACCEPT"]').click()
sleep(1)

cars = []

while True:
    # find all img.category-page__member-thumbnail elements
    images = webdriver.find_elements(By.CSS_SELECTOR, '.category-page__member-thumbnail')
    # for each image, get parent a tag and get href
    for image in images:
        a = image.find_element(By.XPATH, '..')
        href = a.get_attribute('href')
        cars.append(href)
    print(f'---- Found {len(images)} images')

    try:
        # find span with content 'Next'
        next_button = webdriver.find_element(By.XPATH, '//span[text()="Next"]')
        # click the next button
        next_button.click()
    except:
        print('---- No more pages')
        break

    sleep(1)


# open each car, click pi-image-thumbnail, wait, find .media, find first img child, get src and print
with open('../global/data/forza5.txt', 'w') as f:
    for car in tqdm(cars):
        try:
            webdriver.get(car)
            # find a tag with class pi-image-thumbnail
            sleep(3)
            a = webdriver.find_element(By.CSS_SELECTOR, '.pi-image-thumbnail')
            a.click()
            # find .media
            sleep(3)
            div = webdriver.find_element(By.CSS_SELECTOR, '.media')
            # find first img child
            sleep(1)
            img = div.find_element(By.CSS_SELECTOR, 'img')
            src = img.get_attribute('src')
            # save
            f.write(src + '\n')
            print(src)
        except:
            print(f'---- Error on {car}')
            sleep(1)

# close the browser
webdriver.quit()

# after running, go to global/data/forza5.txt and regex search for 'revision.*' and replace with '' (the last part of the link causes issues)