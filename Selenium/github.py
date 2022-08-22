from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class  Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://www.github.com/")
        time.sleep(2)

        self.browser.find_element(By.XPATH, '/html/body/div[1]/header/div/div[2]/div[2]/div[2]/a').click()

        time.sleep(2)

        self.browser.find_element(By.XPATH, '//*[@id="login_field"]').send_keys(f"{self.username}")
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(f"{self.password}")

        time.sleep(2)

        self.browser.find_element(By.XPATH,'//*[@id="login"]/div[4]/form/div/input[12]').click()
        
    def getFollowers(self):

        self.browser.get(f"https://github.com/{self.username}?tab=followers")

        time.sleep(2)

        items = self.browser.find_elements(By.XPATH,'//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]')

        for item in items:
            self.followers.append(item.find_element(By.XPATH, '//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/a/span[1]').text)






    
github = Github("Your User Name","Your Password")
github.signIn()
github.getFollowers()
print(github.followers)