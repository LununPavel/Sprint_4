import allure
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываю страницу приложения')
    def go_to_site(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=10):
        WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator), message=f'Not foud {locator}')

    @allure.step('Нажимаю на элемент клавишей Enter')
    def enter_on_button(self, locator_button):
        self.driver.find_element(*locator_button).send_keys(Keys.ENTER)

    @allure.step('Кликую на элемент')
    def click_on_button(self, locator_button):
        self.driver.find_element(*locator_button).click()

    @allure.step('Получаю урл текущей вкладки')
    def check_current_url(self):
        return self.driver.current_url