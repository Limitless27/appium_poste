import self as self
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
import time

from selenium.webdriver.common.by import By

desired_cap = {
    "platformName": "Android",
    "appium:deviceName": "Android Emulator",
    "appium:appPackage": "com.posteitaliane.spim",
    "appium:appActivity": ".MainActivity"
}
# FIle di properties
appium_service = AppiumService()

appium_service.start(args=['--address', '127.0.0.1', '--port', '4723'])
assert (appium_service.is_running)
assert (appium_service.is_listening)
print("The server is running?"+ str(appium_service.is_running))
print(appium_service.is_listening)
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_cap)
while True:
    try:
        buttonChiudi = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
        buttonChiudi.click()
        buttonPacco = driver.find_element(By.XPATH, '//androidx.recyclerview.widget.RecyclerView[@content-desc="Le tue operazioni"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView')
        buttonPacco.click()
        time.sleep(1)
        appium_service.stop()
    except ValueError:
        print(" ERROR BRO  ")
        pass
    break