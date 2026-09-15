import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False

webdriver = webdriver.Firefox(options=options)
webdriver.get('https://www.deviantart.com/daily-deviations')
sleep(5)
# find banner by .ncmp__banner-inner
banner = webdriver.find_element(By.CSS_SELECTOR, '.ncmp__banner')
webdriver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", banner)

# find button with 'Accept' and click
webdriver.find_element(By.XPATH, '//button[text()="Accept"]').click()

# find element with class _1LNZO and remove 
element = webdriver.find_element(By.CSS_SELECTOR, '._1LNZO')
webdriver.execute_script("""
var element = arguments[0];
element.parentNode.removeChild(element);
""", element)

sleep(2)

# get all elements with data-hook="deviation_link"
links = []
with open('data/deviantart.txt', 'w') as f:
    for _ in range(50):
        elements = webdriver.find_elements(By.CSS_SELECTOR, '[data-hook="deviation_link"]')
        for element in elements:
            try: 
                # get the href attribute
                href = element.get_attribute('href')
                if not href in links:
                    links.append(href)
                    print(href)
                    f.write(href)
                    f.write('\n')
            except:
                pass

        # find a with content 'Next' and click
        sleep(2)
        # scroll to bottom
        webdriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        webdriver.find_element(By.XPATH, '//a[text()="Next"]').click()



# close the browser
webdriver.quit()