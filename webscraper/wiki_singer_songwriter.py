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
webdriver.get('https://en.wikipedia.org/wiki/List_of_singer-songwriters')

# find all links without a class
links_without_classes = webdriver.find_elements(By.XPATH, '//a[not(@class)]')

singer_songwriter_links = []

for link in links_without_classes:
    # check if the parent is of type li with no classes
    parent = link.find_element(By.XPATH, '..')
    if parent.tag_name == 'li' and not parent.get_attribute('class'):
        singer_songwriter_links.append(link)


# for every link, save the href attribute
singer_songwriter_links = [link.get_attribute('href') for link in singer_songwriter_links ]

print(f'Found {len(singer_songwriter_links)} singer-songwriter links')

images = []

# open a txt
with open('../global/data/singer_songwriter_images.txt', 'w') as f:
    for href in tqdm(singer_songwriter_links):
        if not '#' in href and '/wiki/' in href and not 'File:' in href:
            print('---- Checking {}'.format(href))
            webdriver.get(href)
            sleep(.1)
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

print(images)