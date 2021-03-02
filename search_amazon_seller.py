#!/usr/bin/env python3
'''
Automation script to login and search accordingly
'''
from selenium import webdriver
from credentials import *
from configurations import * 
from webdriver_manager.chrome import ChromeDriverManager
import time 

CONFIGURATIONS = {
    'SIGN_IN_CONDITIONS':'//h1[contains(text(),"Sign-In")]'
}
class AmazonSellerCrawl():

    def __init__(self, url):
        self.url = url

    def start_driver(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
        driver.maximize_window()
        return driver 
    def check_sign_in_condition(self, driver):
        '''
        Checks the driver condition if exits
        '''
        print("Checking the sign in conditions of driver")
        time.sleep(2)
        sign_in_element = driver.find_element_by_xpath('//h1[contains(text(),"Sign-In")]')
        if sign_in_element:
            return True
        else:
            return False
    



    def login_amazon_account(self, driver):
        '''
        It helps to login the amazon account
        '''
        time.sleep(1)
        print("Trying to login for amazon")
        time.sleep(1)
        breakpoint()

    
    def search_amazon_seller(self):
        '''
        This is for searching the amazon
        '''
        url = self.url
        driver = self.start_driver()
        if self.check_sign_in_condition(driver):
            print("Need to login first with amazon credentials")
            driver = self.login_amazon_account(driver)
            driver.find_element_by_name('email').send_keys(USERNAME)
            time.sleep(1)
            driver.find_element_by_name('password').send_keys(PASSWORD)
            driver.find_element_by_name('rememberMe').click()
            #checkbox

            time.sleep(1)
            driver.find_element_by_xpath("//span[@class='a-button-inner']").click()
            breakpoint()
        breakpoint()





if __name__ == '__main__':
    print("Starting the Amazon Seller")
    URL = 'https://sellercentral.amazon.com/analytics/dashboard/searchTerms'
    amazon_driver = AmazonSellerCrawl(url=URL)
    amazon_driver.search_amazon_seller()
    breakpoint()

