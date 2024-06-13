import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from pages.base_page import BasePage
from locators.page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC, expected_conditions


class MainPage(BasePage):

    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_section(MainPageLocators.END_OF_PAGE_LOCATOR)
        self.click_to_element(locator_q_formatted)

    def get_text_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    def get_answer_text(self, num):
        self.click_to_question(num)
        return self.get_text_answer(num)






