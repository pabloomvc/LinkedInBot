from selenium import webdriver
from time import sleep
from linkedin_login import email, password
from selenium.webdriver.common.keys import Keys
import random

"""CHANGE THIS VARIABLE FOR THE PATH TO THE WEBDRIVER"""
webdriver_path = r""

class LBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=webdriver_path)
        self.driver.get('https://linkedin.com')

    def login(self):
        login_btn = self.driver.find_element_by_link_text('Inicia sesión')
        login_btn.click()

        sleep(3)

        email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
        email_in.send_keys(email)

        pwd_in = self.driver.find_element_by_xpath('//*[@id="password"]')
        pwd_in.send_keys(password)

        login = self.driver.find_element_by_xpath('//*[@aria-label="Iniciar sesión"]')
        login.click()

    def goto_my_network(self):
        my_network_btn = self.driver.find_element_by_xpath('//nav[@data-nav="main"]//a[@href="/mynetwork/"]')
        my_network_btn.click()

    def click_on_profiles(self):
        while 1:
            try:
                self.goto_my_network()

                profiles = bot.driver.find_elements_by_xpath('//a[@data-control-name="pymk_profile"]/img')
                
                random.shuffle(profiles)
                rand2 = random.random()*3+1
                rand3 = random.random()*3+1

                profiles[0].click()
                sleep(rand2)

                sleep(rand3)
            except Exception: #exception in case the elements of the page havent fully loaded yet
                sleep(2)


bot=LBot()
bot.login()
#sleep(3)
#bot.click_on_profiles()