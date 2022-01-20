import time

from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By

class PagePoste:
    def __init__(self):
        steps.__init__()
        print("Inizializzazione")

class steps:
    def __init__(self):
        self.__steps()
    def __steps(self):
        while True:
            try:
                time.sleep(5)
                buttonChiudi = self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
                buttonChiudi.click()
                buttonPacco = self.driver.find_element(By.XPATH,'//androidx.recyclerview.widget.RecyclerView[@content-desc="Le tue operazioni"]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout/android.widget.TextView')
                buttonPacco.click()
                time.sleep(1)
            except ValueError:
                print(" ERROR BRO  ")
                pass