class Urls:
    MAIN_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_URL = 'https://dzen.ru/?yredirect=true'

class AnswerText:
    ANSWER_TEXT_PRICE = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_TEXT_SOME_SCOOTERS = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_TEXT_RENT_TIME = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_TEXT_TODAY_RENT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_TEXT_EXTEND_TIME = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_TEXT_BATTERY = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_TEXT_CANCELL_ORDER = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_TEXT_COUNTRY = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

class OrderPageData:
    DATA_ORDER_1 = {
        'first_name': 'Яна',
        'last_name': 'Кусь',
        'address': 'Первомайская, 110',
        'station': 'Первомайская',
        'phone_number': '+79994444144',
        'delivery_date': '15.06.2024',
        'rent_days': 'сутки',
        'scooter_colour': 'black',
        'comment': '-'
    }

    DATA_ORDER_2 = {
        'first_name': 'Олег',
        'last_name': 'Сборкин',
        'address': 'Измайловская, 5',
        'station': 'Измайловская',
        'phone_number': '+79994444144',
        'delivery_date': '16.05.2024',
        'rent_days': 'четверо суток',
        'scooter_colour': 'grey',
        'comment': '))))'
    }

    ORDER_CONFIRM_TITLE_TEXT = 'Заказ оформлен'
