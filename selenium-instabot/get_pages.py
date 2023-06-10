from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time




class Getpages:
    def __init__(self, driver):
        self.driver = driver

    def get_followers(self):

        search_bar = WebDriverWait(self.driver,  10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > input")))
        search_bar.click()
        search_bar.send_keys("zim_lmao")

        clk = self.driver.find_element_by_css_selector('#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.LWmhU._0aCwM > div.drKGC > div > a:nth-child(1) > div')
        clk.click()

        follow_btn = WebDriverWait(self.driver,  10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/ul/li[2]/a/span')))
        follow_btn.click()

        popup = WebDriverWait(self.driver,  10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div[2] ")))
        
        self.driver.execute_script("argument[0].scrollTop=arguments[0].scrollHeight", popup)

