from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os

class BrowserClient:
    def __init__(self, browser_type='chrome'):
        self.browser_type = browser_type
        self.driver = self._init_driver()
        self.driver.maximize_window()

    def _get_options(self):
        home_dir = os.environ['USERPROFILE']
        if self.browser_type == 'chrome':
            options = webdriver.ChromeOptions()
            options.add_argument(r"user-data-dir={}\AppData\Local\Google\Chrome\Selenium Data".format(home_dir))
        elif self.browser_type == 'edge':
            options = webdriver.EdgeOptions()
            options.add_argument(r"user-data-dir={}\AppData\Local\Microsoft\Edge\Selenium Data".format(home_dir))
        else:
            raise ValueError('Unsupported browser type')
        options.add_argument("--no-sandbox")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        return options

    def _init_driver(self):
        options = self._get_options()
        if self.browser_type == 'chrome':
            service = webdriver.ChromeService(executable_path=r".\chromedriver.exe")
            return webdriver.Chrome(service=service, options=options)
        elif self.browser_type == 'edge':
            service = webdriver.EdgeService(executable_path=r".\msedgedriver.exe")
            return webdriver.Edge(service=service, options=options)
        else:
            raise ValueError('Unsupported browser type')

    def get(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source

    def wait_for_element(self, by, value, timeout=20):
        WebDriverWait(self.driver, timeout).until(lambda d: d.find_element(by, value).is_displayed())

    def close(self):
        self.driver.close()
