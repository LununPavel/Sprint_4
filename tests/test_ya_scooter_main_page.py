import time
import allure
from pages.ya_scooter_main_page import YaScooterMainPage
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from urls import Urls


class TestCheckAccordion():

    @allure.description('Открываю первую выпадашку и проверяю текст')
    def test_accordion_answer_1(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_1)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_1) == \
               'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('Открываю вторую выпадашку и проверяю текст')
    def test_accordion_answer_2(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_2)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_2) == \
               'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('Открываю третью выпадашку и проверяю текст')
    def test_accordion_answer_3(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_3)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_3) == \
               'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

    @allure.description('Открываю четвертую выпадашку и проверяю текст')
    def test_accordion_answer_4(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_4)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_4) == \
               'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.description('Открываю пятую выпадашку и проверяю текст')
    def test_accordion_answer_5(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_5)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_5) == \
               'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('Открываю шестую выпадашку и проверяю текст')
    def test_accordion_answer_6(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_6)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_6) == \
               'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('Открываю седьмую выпадашку и проверяю текст')
    def test_accordion_answer_7(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_7)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_7) == \
               'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('Открываю восьмую выпадашку и проверяю текст')
    def test_accordion_answer_8(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_accordion_button(LocatorMainYaScooterPage.QUESTION_ACCORDION_BUTTONS_8)
        assert ya_scooter_main_page.return_text_answer_accordion(LocatorMainYaScooterPage.ANSWER_ACCORDION_8) == \
               'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    @allure.description('Перехожу на страницу яндекса и проверяю урл')
    def test_go_to_yandex_page_through_yandex_button(self, driver):
        ya_scooter_main_page = YaScooterMainPage(driver)
        ya_scooter_main_page.go_to_site(Urls.url_main_page)
        ya_scooter_main_page.click_on_button(LocatorMainYaScooterPage.YANDEX_BUTTON)
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        assert ya_scooter_main_page.check_current_url() == "https://dzen.ru/?yredirect=true"


