
from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.jpg")

url = "https://github.com/ali-osman-de"
driver.get(url)

if "ali-osman-de" in driver.title:
    driver.save_screenshot("github-ali-osman-de.jpg")

time.sleep(2)

driver.back()

time.sleep(2)

print(driver.title)

time.sleep(2)
driver.close()