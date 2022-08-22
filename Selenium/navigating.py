from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "https://github.com"
driver.get(url)

searchInput = driver.find_element(By.CSS_SELECTOR, '[name="q"]')
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_elements(By.CLASS_NAME, 'v-align-middle')

for element in result:
    print(element.text)


driver.close()