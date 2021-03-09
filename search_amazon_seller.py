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
    'SIGN_IN_CONDITIONS':'//h1[contains(text(),"Sign-In")]',
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
    
    def get_reporting_range(self, driver, range_='Weekly'):
        '''Options for range are
        * Daily
        * Weekly
        * Monthly
        * Quarterly
        It will select the the data and download the file
        '''
        time.sleep(1)
        driver.find_element_by_xpath("//span[contains(text(),'Reporting Range')]/parent::span/parent::span/parent::button").click()
        driver.find_element_by_xpath(f'//li[@aria-label="{range_}"]').click()

        return driver


    def search_item(self, driver, search_item='iphone'):
        '''Insert the search terms in the file
        '''
        time.sleep(2)
        driver.find_element_by_xpath('//input[contains(@class,"searchbar")]').send_keys(search_item)
        driver.find_element_by_xpath('//span[contains(text(),"Apply")]/parent::button')
        time.sleep(3)
        return driver
        #



    def login_amazon_account(self, driver):
        '''
        It helps to login the amazon account
        '''
        time.sleep(1)
        print("Trying to login for amazon")
        time.sleep(1)
        driver.find_element_by_name('email').send_keys(USERNAME)
        time.sleep(1)
        driver.find_element_by_name('password').send_keys(PASSWORD)
        driver.find_element_by_name('rememberMe').click()
        time.sleep(1)
        driver.find_element_by_xpath("//span[@class='a-button-inner']").click()
        breakpoint()
        # we need to perform some manual_task here  
        # Now choosing the range
        return driver

    
    def download_excel_file(self, driver):
        '''This is for downloading the excel_file
        '''
        #selecting the download 
        time.sleep(1)
        driver.find_element_by_xpath('//span[contains(text(),"Download")]/parent::button').click()
        driver.find_element_by_xpath('//li[contains(@aria-label,"As Excel Workbook")]').click()
        return driver


    def search_amazon_seller(self):
        '''
        This is for searching the amazon
        '''
        url = self.url
        driver = self.start_driver()
        if self.check_sign_in_condition(driver):
            print("Need to login first with amazon credentials")
            driver = self.login_amazon_account(driver)
            
            #checkbox

            time.sleep(1)
            # get_daily
            driver = self.get_reporting_range(driver=driver)
            time.sleep(1)
            driver = self.search_item(driver=driver)
            time.sleep(1)
            driver = self.download_excel_file(driver=driver)
            breakpoint()
            
        breakpoint()





if __name__ == '__main__':
    print("Starting the Amazon Seller")
    URL = 'https://sellercentral.amazon.com/analytics/dashboard/searchTerms'
    amazon_driver = AmazonSellerCrawl(url=URL)
    amazon_driver.search_amazon_seller()
    breakpoint()

