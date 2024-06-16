import allure

from pages import order_page
from pages.order_page import OrderPage


class TestRedirect:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката со старницы заказа')
    def test_open_main_page_when_click_on_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_scooter()
        expected_url = order_page.get_url_main_page()
        assert order_page.get_url_main_page() == expected_url

    @allure.title('Проверка открытия нового окна станицы Дзена по клику на лого Яндекса')
    def test_open_dzen_in_new_window(self, driver):
        order_page = OrderPage(driver)
        order_page.open_order_page()
        order_page.click_on_logo_yandex()
        order_page.switch_to_new_window()
        expected_url = order_page.get_url_dzen_page()
        assert order_page.get_url_dzen_page() == expected_url, 'URL не соответствует странице Дзена'

