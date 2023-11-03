import time

from selenium.webdriver.common.by import By
from launch_browser import Launch


class StartPage(Launch):
    URL = 'https://google.com/maps'

    def __init__(self):
        super().__init__()

    def open_start_page(self):
        self.driver.get(StartPage.URL)
        time.sleep(3)

    def search_place(self, place):
        # Находим поле для поиска локаций
        search_input = self.driver.find_element(By.ID, 'searchboxinput')
        search_input.send_keys(place)
        button_for_search = self.driver.find_element(By.ID, 'searchbox-searchbutton')
        button_for_search.click()
        time.sleep(3)

    def check_title(self, title):
        # Проверяем титульную страницу
        assert self.driver.title == title




