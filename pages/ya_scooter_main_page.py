import allure
from locators.ya_scooter_main_page_locators import LocatorMainYaScooterPage
from locators.yandex_browser_main_page import LocatorYandexBrowserMainPage
from pages.base_page import BasePage


class YaScooterMainPage(BasePage):

    @allure.step('Получаю текст элемента')
    def get_text_main_page(self):
        return self.get_text(LocatorYandexBrowserMainPage.NAVIGATION_BAR)

    def click_on_button_main_page(self):
        self.click_on_button(LocatorMainYaScooterPage.YANDEX_BUTTON)