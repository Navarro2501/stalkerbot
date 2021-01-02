from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import time

username = "your username"
password = "your password"
target_account = "grimes (I love your music!)"
chrome_driver_path = "your chrome driver path"

class InstagramFollowerBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.maximize_window()
        self.driver.get("https://www.instagram.com/")
        time.sleep(3)

    
    def login(self):
        # Login
        try:
            self.driver.find_element_by_name('username').send_keys(username)
            self.driver.find_element_by_name('password').send_keys(password)
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        except NoSuchElementException:
            print("Error with localization elements\n" + str(NoSuchElementException))
        time.sleep(5)
        
        # Rejection of login credentials save
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except NoSuchElementException:
            print("Rejection of login credentials save failed: element did not display or xpath is wrong. " + str(NoSuchElementException))
        time.sleep(7)
        
        # Disable notifications
        try:
            self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        except NoSuchElementException:
            print("Did not find the option to disable notifications: " + str(NoSuchElementException))        
        time.sleep(2)

        # Getting to the target account
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div/div/span[2]').click()
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(target_account)
            time.sleep(5)
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]').click()
        except NoSuchElementException:
            print("Did not find the option to enter target account: " + str(NoSuchElementException))
        time.sleep(5)

        self.find_followers()

    def find_followers(self):
        # Following the people
        try:
            self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
            time.sleep(3)

            modal = self.driver.find_element_by_xpath('html/body/div[5]/div/div/div[2]')
            for i in range(150):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                time.sleep(2)
            elements = self.driver.find_elements_by_css_selector('.sqdOP.L3NKy.y3zKF')            
            for element in elements:
                if element.text == "Follow":
                    try:
                        element.click() 
                    except ElementClickInterceptedException:
                        cancel_button = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
                time.sleep(3.5)
        except NoSuchElementException:
            print("Could not get the pictures: " + str(NoSuchElementException))