from selenium import webdriver


class Launch:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def close_browser(self):
        self.driver.close()