import allure
from data import AnswerText
import pytest
from pages.main_page import MainPage

class TestMainPage:

    @allure.title('Проверка блока "Вопросы о важном"')
    @allure.description('При нажатии на вопрос должен открываться текст ответа')
    @pytest.mark.parametrize('num, result', [
        (0, AnswerText.ANSWER_TEXT_PRICE),
        (1, AnswerText.ANSWER_TEXT_SOME_SCOOTERS),
        (2, AnswerText.ANSWER_TEXT_RENT_TIME),
        (3, AnswerText.ANSWER_TEXT_TODAY_RENT),
        (4, AnswerText.ANSWER_TEXT_EXTEND_TIME),
        (5, AnswerText.ANSWER_TEXT_BATTERY),
        (6, AnswerText.ANSWER_TEXT_CANCELL_ORDER),
        (7, AnswerText.ANSWER_TEXT_COUNTRY)
    ]
    )
    def test_questions_and_answers(self, driver, num, result):
        main_page = MainPage(driver)
        main_page.open_main_page()
        assert main_page.get_answer_text(num) == result