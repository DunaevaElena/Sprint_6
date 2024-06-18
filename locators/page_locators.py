from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = [By.XPATH, './/div[@id="accordion__heading-{}"]']
    ANSWER_LOCATOR = [By.XPATH, '//div[@id="accordion__panel-{}"]']
    END_OF_PAGE_LOCATOR = [By.ID, "accordion__heading-7"]



class OrderPageLocators:
    FORM1_TITLE = [By.XPATH, "//div[contains(@class, 'Order_Header')]"]
    NAME_LOCATOR = [By.CSS_SELECTOR, "input[placeholder='* Имя']"]
    LASTNAME_LOCATOR = [By.CSS_SELECTOR, "input[placeholder='* Фамилия']"]
    ADDRESS_LOCATOR = [By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']"]
    METRO_SEARCH_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Станция метро']"]
    SELECT_STATION = [By.XPATH, ".//div[text()='{}']"]
    PHONE_NUMBER_INPUT_FIELD = [By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"]
    BUTTON_NEXT = [By.XPATH, "//button[text()='Далее']"]

    FORM2_TITLE = [By.XPATH, "//div[@class='Order_Header__BZXOb']"]
    DATE_DELIVERY = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    SELECTED_DATE = [By.XPATH, "//div[contains(@class, 'react-datepicker__day--selected')]"]
    RENT_TIME = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]
    SELECT_RENT_TIME = [By.XPATH, ".//div[text()='{}']"]
    COLOR_CHECKBOX = [By.ID, '{}']
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "(.//button[text()='Заказать'])[2]"]

    ORDER_CONFIRM = [By.XPATH, "//div[text()='Хотите оформить заказ?']"]
    YES_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_COMPLETED = [By.XPATH, ".//div[text() = 'Заказ оформлен']"]
    SCOOTER_BUTTON = [By.XPATH, ".//a[@href='/']"]
    YANDEX_BUTTON = [By.XPATH, ".//a[@href='//yandex.ru']"]
    PAGE_TITLE = [By.XPATH, "//div[contains(@class, 'Home_Header')]"]
