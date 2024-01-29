from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait


class WebDriver:

    """
    Instantiate Webdriver with chrome settings and etc.
    """

    def __init__(self, chromeOptions, executable_path, config_vars):
        for vars in config_vars["chrome_options"].values():
            chromeOptions.add_argument(vars)

        self.caps = DesiredCapabilities.CHROME.copy()
        self.caps["acceptInsecureCerts"] = True

        self.driver = webdriver.Chrome(
            executable_path=executable_path,
            chrome_options=chromeOptions,
            desired_capabilities=self.caps,
        )

        self.wait = WebDriverWait(self.driver, 80)

    def get_chrome_webdriver(self):
        return self.driver

    def get_chrome_wait(self):
        return self.wait

    def change_webdriver_waiting_time(self, time_in_seconds):
        self.wait = WebDriverWait(self.driver, time_in_seconds)
        return self.wait.until
