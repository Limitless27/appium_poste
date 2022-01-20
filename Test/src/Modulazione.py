import contextlib
import unittest

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import page_poste

import time
from selenium.webdriver.common.by import By
class Modulazione(unittest.FunctionTestCase):
    desired_cap={}
    driver = None
    # FIle di properties
    def setUp(self):
        page_poste= self.page_poste.PagePoste.__init__(self)
        self.desired_cap = {
            "platformName": "Android",
            "appium:deviceName": "Android Emulator",
            "appium:appPackage": "com.posteitaliane.spim",
            "appium:appActivity": ".MainActivity"
        }
        #main
        #start appium Server
        self.appium_service = AppiumService()
        self.appium_service.start(args=['--address', '127.0.0.1', '--port', '4723'])
        assert (self.appium_service.is_running)
        assert (self.appium_service.is_listening)
        #start application on device
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_cap)
        Modulazione.__testFirstAutomation(self)

    def __testFirstAutomation(self):
            try:
                self.page_poste.__steps()
                self.appium_service.stop()
            except ValueError:
                print(" ERROR BRO  ")
                pass