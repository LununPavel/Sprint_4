import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage


class YaScooterOrderPage(BasePage):

    @allure.step('Ввожу текст в поле')
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Выбираю станцию метро')
    def select_station(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.DOWN)
        a.send_keys(Keys.ENTER)

    @allure.step('Выбираю текущую дату')
    def select_current_date(self, locator):
        a = self.driver.find_element(*locator)
        a.click()
        a.send_keys(Keys.ENTER)

    @allure.step('Выбираю срок использования')
    def select_rental_period(self, locator, period_value):
        self.driver.find_element(*locator).click()
        self.driver.find_element(*period_value).click()

    @allure.step('Получаю текст элемента')
    def return_text(self, locator):
        return self.driver.find_element(*locator).text