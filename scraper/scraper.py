from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


199.36.158.100









def domain():
    url = "https://www.secureserver.net/products/domain-registration/find?plid=509568&domainToCheck=gamkrib"
    driver = Chrome(executable_path = "C:/Users/shaphat/Desktop/PROJECTS/FUN PROJECTS/domain_search/scraper/chromedriver.exe")
    driver.get(url)
    delay = 120

    try:
        data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'main-price')))
        

        print(data.text)
        #print(price.text)
    except TimeoutException:
        print ("Loading took too much time!")

    driver.quit()

domain()


def bluehost():
    url = "https://www.hover.com/domains/results?utf8=%E2%9C%93&q=gamkrib"
    driver = Chrome(executable_path = "C:/Users/shaphat/Desktop/PROJECTS/FUN PROJECTS/domain_search/scraper/chromedriver.exe")
    driver.get(url)
    delay = 120

    try:
        data = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.CLASS_NAME, 'price')))
        

        print(data.text)
        #print(price.text)
    except TimeoutException:
        print ("Loading took too much time!")

    driver.quit()

#bluehost()
