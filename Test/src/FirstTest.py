import unittest
from unittest import TestCase

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from method_object import Methods
from elementPage import Elements

class Test(TestCase):

    def test_1(self):
        #try:
            methods = Methods()
            elements = Elements()
            print(methods.desired_cap)
            desired = methods.details()
            driver = methods.AppiumServiceStart(desired)
            driver.implicitly_wait(0)
            #driver.implicitly_wait(1000)
            if len(driver.find_elements(By.XPATH, elements.labelBenvenutoIn))>0:
                driver.find_element(By.XPATH, elements.benvenutoButtons1).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons2).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons3).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons4).click()
                driver.find_element(By.XPATH, elements.buttonScegliUffPostale).click()
            if len(driver.find_elements(By.XPATH, elements.buttonClose))>0:
                driver.find_element(By.XPATH, elements.buttonClose).click()
            #driver.find_element(By.XPATH, elements.buttonPacco).click()
            driver.find_element(By.XPATH, elements.buttonMenu).click()
            driver.find_element(By.XPATH, elements.buttonAccediMenu).click()
            driver.find_element(By.XPATH, elements.inputTextUsername).set_text('anna.aversano')
            driver.find_element(By.XPATH, elements.inputTextPassword).set_text('Password1!')
            driver.find_element(By.XPATH, elements.buttonAccedi).click()
            driver.implicitly_wait(1000)
            if len(driver.find_elements(By.XPATH, elements.labelBenvenutoIn))>0:
                driver.find_element(By.XPATH, elements.benvenutoButtons1).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons2).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons3).click()
                driver.find_element(By.XPATH, elements.benvenutoButtons4).click()
                driver.find_element(By.XPATH, elements.buttonScegliUffPostale).click()
            methods.appium_service.stop()
        #except:
            #print("An exception occurred")

if __name__ == '__main__':
    unittest.main()