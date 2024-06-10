import time

import allure
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from pages.base_page import BasePage
from locators.page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)
    @allure.step("Клик на вопрос")
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        element = self.find_element(MainPageLocators.END_OF_PAGE_LOCATOR)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(3)
        self.click_to_element(locator_q_formatted)

    @allure.step("Получение текста ответа")
    def get_text_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step("Проверка текста ответа")
    def get_answer_text(self, num):
        self.click_to_question(num)
        return self.get_text_answer(num)






