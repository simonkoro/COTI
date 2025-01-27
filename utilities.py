import subprocess
import time as t
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Utilities:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def control_metamask_window(self):
        t.sleep(1)
        opened_windows = self.driver.window_handles
        try:
            for window in opened_windows:
                self.driver.switch_to.window(window)
                if "MetaMask" == self.driver.title:
                    break
        except Exception as e:
            print("Error acquired while moving to MetaMask pop-up", e)

    def control_coti_window(self):
        t.sleep(1)
        opened_windows = self.driver.window_handles
        try:
            self.driver.switch_to.window(opened_windows[0])
        except Exception as e:
            print("Error acquired while moving back to COTI website:", e)
