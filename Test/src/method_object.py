from appium import webdriver
from appium.webdriver.appium_service import AppiumService
# Define the class

class Methods:
    desired_cap = {}
    appium_service = AppiumService()
    # Define the method

    def details(self):
        desired_cap = {
            "platformName": "Android",
            "appium:deviceName": "Android Emulator",
            "appium:appPackage": "com.posteitaliane.spim",
            "appium:appActivity": ".MainActivity"
        }
        return desired_cap
    def AppiumServiceStart(self, desired_cap):
        appium_service = self.appium_service
        appium_service.start(args=['--address', '127.0.0.1', '--port', '4729'])
        assert (appium_service.is_running)
        assert (appium_service.is_listening)
        # start application on device
        driver = webdriver.Remote('http://127.0.0.1:4729/wd/hub', desired_cap)
        #driver.update_settings({"ignoreUnimportantViews": True})
        return driver



