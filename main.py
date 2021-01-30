from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_path = "C:\webdrivers\chromedriver.exe"

USERNAME = ""
PASSWORD = ""


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(chrome_path)

    def login(self):
        self.driver.get("https://instagram.com")
        time.sleep(2)

        fields = self.driver.find_elements_by_tag_name("input")
        fields[0].send_keys(USERNAME)
        fields[1].send_keys(PASSWORD)
        fields[1].send_keys(Keys.ENTER)
        time.sleep(3)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        followers_link = self.driver.find_element_by_partial_link_text("k followers")
        followers_link.click()
        time.sleep(2)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
        time.sleep(1)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
