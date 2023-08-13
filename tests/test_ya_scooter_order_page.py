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
        ya_scooter_order_page.enter_on_button(LocatorMainYaScooterPage.ORDER_BUTTON_IN_HEADER)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_FIRST_NAME, "Павел")
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_LAST_NAME, "Лунин")
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_ADDRESS, "г. Москва, д. 66")
        ya_scooter_order_page.select_station(LocatorOrderYaScooterPage.FIELD_STATION)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_PHONE_NUMBER, "+71111111111")
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_NEXT)

        ya_scooter_order_page.select_current_date(LocatorOrderYaScooterPage.FIELD_DELIVERY_DATE)
        ya_scooter_order_page.select_rental_period(LocatorOrderYaScooterPage.FIELD_RENTAL_PERIOD, LocatorOrderYaScooterPage.RENTAL_PERIOD_VALUE_1)
        ya_scooter_order_page.click_on_button(LocatorOrderYaScooterPage.SCOOTER_BLACK_COLOR_CHECKBOX)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_COMMENT, "Оплата картой")
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_MIDDLE)
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_YES)

        assert "Заказ оформлен" in ya_scooter_order_page.return_text(LocatorOrderYaScooterPage.SUCCESSFUL_ORDER)

    @allure.description('Оформляю заказ через среднюю кнопку и проверяю, что заказ оформился')
    def test_order_via_middle_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.enter_on_button(LocatorMainYaScooterPage.ORDER_BUTTON_IN_MIDDLE)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_FIRST_NAME, "Иван")
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_LAST_NAME, "Иванов")
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_ADDRESS, "г. Санкт-Петербург, д. 99")
        ya_scooter_order_page.select_station(LocatorOrderYaScooterPage.FIELD_STATION)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_PHONE_NUMBER, "+79999999999")
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_NEXT)

        ya_scooter_order_page.select_current_date(LocatorOrderYaScooterPage.FIELD_DELIVERY_DATE)
        ya_scooter_order_page.select_rental_period(LocatorOrderYaScooterPage.FIELD_RENTAL_PERIOD, LocatorOrderYaScooterPage.RENTAL_PERIOD_VALUE_2)
        ya_scooter_order_page.click_on_button(LocatorOrderYaScooterPage.SCOOTER_GREY_COLOR_CHECKBOX)
        ya_scooter_order_page.enter_text(LocatorOrderYaScooterPage.FIELD_COMMENT, "Оплата наличными")
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_MIDDLE)
        ya_scooter_order_page.enter_on_button(LocatorOrderYaScooterPage.BUTTON_ORDER_YES)

        assert "Заказ оформлен" in ya_scooter_order_page.return_text(LocatorOrderYaScooterPage.SUCCESSFUL_ORDER)

    @allure.description('Проверяю, что по нажатию на кнопку "Самокат" открывается главная страница')
    def test_go_to_main_page_through_scooter_button(self, driver):
        ya_scooter_order_page = YaScooterOrderPage(driver)
        ya_scooter_order_page.go_to_site(Urls.url_main_page)
        ya_scooter_order_page.enter_on_button(LocatorMainYaScooterPage.ORDER_BUTTON_IN_HEADER)
        ya_scooter_order_page.click_on_button(LocatorOrderYaScooterPage.SCOOTER_BUTTON)

        assert ya_scooter_order_page.return_text(LocatorMainYaScooterPage.BLOCK_WITH_QUESTIONS) == "Вопросы о важном"