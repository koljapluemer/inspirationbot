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
webdriver.get('http://127.0.0.1:5500/k/main.html')

# get all images
images = webdriver.find_elements(By.TAG_NAME, 'img')
# for eacht, use execute script to get the width and height
for image in images:
    width = webdriver.execute_script("return arguments[0].width", image)
    height = webdriver.execute_script("return arguments[0].height", image)
    src = image.get_attribute('src').split('/')[-1]
    # convert myfigure.png -resize 200x100 myfigure.jpg
    print(f'convert {src} -resize {width}x{height} {src}')