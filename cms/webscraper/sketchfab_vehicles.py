import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)
webdriver.get(
    'https://sketchfab.com/3d-models/categories/cars-vehicles?features=staffpicked&sort_by=-likeCount&cursor=cD01MzA%3D')
sleep(5)

# scroll all the way down (with js, do several times)
for _ in range(20):
    webdriver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);")
    sleep(2)
    # TODO: currently Load More must be clicked manually because Selenium can't find button

with open('global/data/sketchfab_vehicles.txt', 'w') as f:
    # find all with class="model-name__label"
    links = webdriver.find_elements(By.CSS_SELECTOR, '.model-name__label')
    for link in links:
        href = link.get_attribute('href')
        f.write(href)
        f.write('\n')