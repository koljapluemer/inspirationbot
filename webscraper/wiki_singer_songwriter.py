import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options
from tqdm import tqdm


options = Options()
options.headless = True

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
with open('data/singer_songwriter_images.txt', 'w') as f:
    for artist_page in tqdm(singer_songwriter_links):
        print(f'---- Checking {artist_page}')
        try: 
            # open the link 
            webdriver.get(artist_page)
            # check if there is an .infobox-image
            if webdriver.find_elements(By.CSS_SELECTOR, '.infobox-image'):
                # get the image
                image = webdriver.find_element(By.CSS_SELECTOR, '.infobox-image').find_element(By.TAG_NAME, 'img')
                # append image url to list
                images.append(image.get_attribute('src'))
                # write image url to txt
                f.write(image.get_attribute('src'))
                # newline
                f.write('\n')
        except:
            print(f'---- Error on {artist_page}')

        sleep(.1)

print(images)