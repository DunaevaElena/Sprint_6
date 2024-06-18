import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элемент с ожиданием закрузки')
    def find_element_with_wait(self, locator):
        self.wait_for_load_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент')
    def click_to_element(self, locator):
        self.wait_for_load_element(locator)
        self.driver.find_element(*locator).click()

    @allure.step('Добавить текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    @allure.step('Получить текст с элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.step('Открыть страницу')
    def open_page(self, page_url):
        self.driver.get(page_url)

    @allure.step('Сформировать локатор')
    def format_locators(self, locator_1, num):
        method, locator = locator_1
        locator = locator.format(num)
        return (method, locator)

    @allure.step('Найти элемент без ожидания')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Скролл до секции')
    def scroll_to_section(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Ожидание закрузки элемента')
    def wait_for_load_element(self, locator):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание загрузки страницы')
    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(page_url))

    @allure.step('Переход в новое окно')
    def switch_to_new_window(self):
        return self.driver.switch_to.window(self.driver.window_handles[1])
