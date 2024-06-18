
import allure
from data import Urls
from pages.base_page import BasePage
from locators.page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Открытие главной страницы')
    def open_main_page(self):
        self.open_page(Urls.MAIN_PAGE_URL)

    @allure.step('Клик на вопрос')
    def click_to_question(self, num):
        locator_q_formatted = self.format_locators(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_section(MainPageLocators.END_OF_PAGE_LOCATOR)
        self.click_to_element(locator_q_formatted)

    @allure.step('Поиск ответа на вопрос')
    def get_text_answer(self, num):
        locator_a_formatted = self.format_locators(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_element(locator_a_formatted)

    @allure.step('Получение текста ответа')
    def get_answer_text(self, num):
        self.click_to_question(num)
        return self.get_text_answer(num)






