import allure
from selenium.webdriver import Keys
from pages.base_page import BasePage


class YaScooterMainPage(BasePage):

    @allure.step('Нажимаю на элемент клавишей Enter')
    def click_on_accordion_button(self, locator_question):
        self.driver.find_element(*locator_question).send_keys(Keys.ENTER)

    @allure.step('Получаю текст элемента')
    def return_text_answer_accordion(self, locator_answer):
        return self.driver.find_element(*locator_answer).text