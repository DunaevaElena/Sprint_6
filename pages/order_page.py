from data import OrderPageData, Urls
from locators.page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def set_order(self, data_order):
    #заполнение первой страницы
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, data_order['first_name'])
        self.add_text_to_element(OrderPageLocators.LASTNAME_LOCATOR, data_order['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, data_order['address'])
        self.set_metro_station(data_order['station'])
        self.add_text_to_element(OrderPageLocators.PHONE_NUMBER_INPUT_FIELD, data_order['phone_number'])
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)
        self.wait_for_load_element(OrderPageLocators.FORM2_TITLE)
    #заполнение второй страницы
        self.add_text_to_element(OrderPageLocators.DATE_DELIVERY, data_order['delivery_date'])
        self.click_to_element(OrderPageLocators.SELECTED_DATE)
        self.wait_for_load_element(OrderPageLocators.RENT_TIME)
        self.set_rent_days(data_order['rent_days'])
        self.set_scooter_color(data_order['scooter_colour'])
        self.add_text_to_element(OrderPageLocators.COMMENT_FIELD, data_order['comment'])
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
        self.wait_for_load_element(OrderPageLocators.ORDER_CONFIRM)
        self.click_to_element(OrderPageLocators.YES_BUTTON)


    def set_metro_station(self, station):
        self.click_to_element(OrderPageLocators.METRO_SEARCH_FIELD)
        method, station_loc = OrderPageLocators.SELECT_STATION
        station_locator_with_name = (method, station_loc.format(station))
        self.scroll_to_section(station_locator_with_name)
        self.click_to_element(station_locator_with_name)


    def set_rent_days(self, rent_days):
        self.click_to_element(OrderPageLocators.RENT_TIME)
        method, rent_days_loc = OrderPageLocators.SELECT_RENT_TIME
        rent_days_locator_with_period = (method, rent_days_loc.format(rent_days))
        self.click_to_element(rent_days_locator_with_period)


    def set_scooter_color(self, scooter_color):
        method, checkbox_loc = OrderPageLocators.COLOR_CHECKBOX
        checkbox_locator_with_color = (method, checkbox_loc.format(scooter_color))
        self.click_to_element(checkbox_locator_with_color)


    def open_order_page(self):
        self.open_page(Urls.ORDER_PAGE_URL)


    def wait_for_load_form(self):
        self.wait_for_load_element(OrderPageLocators.FORM1_TITLE)


    def wait_for_load_order_completed(self):
        self.wait_for_load_element(OrderPageLocators.ORDER_COMPLETED)


    def get_actual_result(self):
        actual_result = self.find_element(OrderPageLocators.ORDER_COMPLETED).text
        return actual_result


    def get_expected_result(self):
        expected_result = OrderPageData.ORDER_CONFIRM_TITLE_TEXT
        return expected_result


    def click_on_logo_scooter(self):
        self.click_to_element(OrderPageLocators.SCOOTER_BUTTON)


    def click_on_logo_yandex(self):
        self.click_to_element(OrderPageLocators.YANDEX_BUTTON)


    def wait_for_load_page_title(self):
        self.wait_for_load_element(OrderPageLocators.PAGE_TITLE)


    def wait_for_open_dzen(self):
        self.wait_for_open_page(Urls.DZEN_URL)


    def get_url_main_page(self):
        return Urls.MAIN_PAGE_URL


    def get_url_dzen_page(self):
        return Urls.DZEN_URL


    def check_order(self, locator):
        return self.get_text_from_element(locator)



