from abc import ABC
from appium.webdriver.appium_service import AppiumService
import os
import subprocess

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, NoSuchWindowException, TimeoutException, InvalidSessionIdException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class Appium(ABC):
    """
    Abstract method to run Appium Node server on port 4723
    With staticmethod to kill the server
    """

    device_name = None


    def start_appium_server(self):
        appium_service = AppiumService()


        appium_service.start(args=['--port', '4723', '--session-override', '-bp', '100', '--default-capabilities',
                                   "{\"udid\":\"emulator-5554\",\"systemPort\":8200}"], stdout=subprocess.PIPE, timeout_ms=120000)
        # appium_service.start()

        print(appium_service.is_running)
        print(appium_service.is_listening)

        # print(appium_service.is_listening)


    def connect_selenium_appium_server(self, config):

        self.desired_capabilities = config['desired_caps']
        self.host = config['host']['host_url']

        self.driver = webdriver.Remote(command_executor=self.host, desired_capabilities=self.desired_capabilities)
        self.wait = WebDriverWait(self.driver, 30)
        time.sleep(2)

        # print(self.driver.get_log('server'))

        print(self.driver.session_id)


    def delete_all_appium_packages(self):

        os.system(f'adb -s {self.device_name} uninstall io.appium.uiautomator2.server')
        time.sleep(2)
        os.system(f'adb -s {self.device_name} uninstall io.appium.uiautomator2.server.test')
        time.sleep(2)
        os.system(f'adb -s {self.device_name} uninstall io.appium.unlock')
        time.sleep(2)
        os.system(f'adb -s {self.device_name} uninstall io.appium.settings')
        time.sleep(2)
        """
        adb uninstall io.appium.uiautomator2.server
adb uninstall io.appium.uiautomator2.server.test
adb uninstall io.appium.unlock
adb uninstall io.appium.settings
"""



    def get_emulator_driver(self):
        return self.driver

    def get_emulator_wait(self):
        return self.wait.until

    def get_By(self):
        return By

    def get_Ec(self):
        return EC

    def get_Exceptions(self):
        return NoSuchElementException, TimeoutException, StaleElementReferenceException

    def change_emulator_waiting_time(self, time_in_seconds):
        self.wait = WebDriverWait(self.driver, time_in_seconds)
        return self.wait.until

    def get_action_chains(self):
        return ActionChains(self.driver)

    @staticmethod
    def kill_appium_server(port=None):
        if port:

            os.system(f"kill -9 $(lsof -i tcp:{port})")

        else:

            os.system("kill -9 $(lsof -i tcp:4723)")




if __name__ == "__main__":
    Appium()
    # call_abstract = CallABC()

