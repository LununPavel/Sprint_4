import allure
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from locators.ya_scooter_order_page_locators import LocatorOrderYaScooterPage
from pages.ya_scooter_order_page import YaScooterOrderPage
from urls import Urls


class TestCreateOrder():

    @allure.description('Оформляю заказ через верхнюю кнопку и проверяю, что заказ оформился')
    def test_order_via_top_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.fill_field_for_order_via_top_button()

        assert "Заказ оформлен" in ya_scooter_order_page.get_text_successful_order()

    @allure.description('Оформляю заказ через среднюю кнопку и проверяю, что заказ оформился')
    def test_order_via_middle_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.fill_field_for_order_via_middle_button()

        assert "Заказ оформлен" in ya_scooter_order_page.get_text_successful_order()

    @allure.description('Проверяю, что по нажатию на кнопку "Самокат" открывается главная страница')
    def test_go_to_main_page_through_scooter_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.enter_on_button_order_in_header()
        ya_scooter_order_page.click_on_button_scooter()

        assert ya_scooter_order_page.get_text_block_with_questions() == "Вопросы о важном"