import allure
import pytest
from locators.yandex_browser_main_page import LocatorYandexBrowserMainPage
from pages.ya_scooter_main_page import YaScooterMainPage
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from static_data import StaticData
from urls import Urls


class TestCheckAccordion():

    @allure.description('Открываю первую выпадашку и проверяю текст')
    @pytest.mark.parametrize('question,answer,answer_on_question',
                             [
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_1, LocatorMainYaScooterPage.ANSWER_ACCORDION_1, StaticData.answers_on_questions[0]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_2, LocatorMainYaScooterPage.ANSWER_ACCORDION_2, StaticData.answers_on_questions[1]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_3, LocatorMainYaScooterPage.ANSWER_ACCORDION_3, StaticData.answers_on_questions[2]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_4, LocatorMainYaScooterPage.ANSWER_ACCORDION_4, StaticData.answers_on_questions[3]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_5, LocatorMainYaScooterPage.ANSWER_ACCORDION_5, StaticData.answers_on_questions[4]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_6, LocatorMainYaScooterPage.ANSWER_ACCORDION_6, StaticData.answers_on_questions[5]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_7, LocatorMainYaScooterPage.ANSWER_ACCORDION_7, StaticData.answers_on_questions[6]],
                                 [LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_8, LocatorMainYaScooterPage.ANSWER_ACCORDION_8, StaticData.answers_on_questions[7]]
                             ])
    def test_accordion_answer(self, driver, question, answer, answer_on_question):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.enter_on_button(question)
        ya_scooter_main_page.find_element(answer)
        assert ya_scooter_main_page.get_text(answer) == answer_on_question


    @allure.description('Перехожу на страницу яндекса и проверяю загрузку страницы')
    def test_go_to_yandex_page_through_yandex_button(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_button_main_page()
        driver.switch_to.window(driver.window_handles[1])
        ya_scooter_main_page.find_element(LocatorYandexBrowserMainPage.NAVIGATION_BAR)
        assert ya_scooter_main_page.get_text_main_page() == "Новости"


