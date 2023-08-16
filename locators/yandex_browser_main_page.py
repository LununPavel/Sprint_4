from selenium.webdriver.common.by import By


class LocatorYandexBrowserMainPage:
    NAVIGATION_BAR = (By.XPATH, "//div[contains(text(),'Новости')]")