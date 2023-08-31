from selenium.webdriver.common.by import By


class LocatorMainYaScooterPage:
    YANDEX_BUTTON = (By.XPATH, "//img[@alt='Yandex']")
    SCOOTER_BUTTON = (By.XPATH, "//img[@alt='Scooter']")

    ORDER_BUTTON_IN_HEADER = (By.XPATH, "//div[contains(@class,'Header_Nav')]/button[contains(@class,'Button_Button')]")
    ORDER_BUTTON_IN_MIDDLE = (By.XPATH, "//button[contains(@class,'Button_Middle')]")

    QUESTION_ACCORDION_BUTTONS_1 = (By.ID, "accordion__heading-0")
    ANSWER_ACCORDION_1 = (By.XPATH, "//div[@id='accordion__panel-0']/p")
    QUESTION_ACCORDION_BUTTONS_2 = (By.ID, "accordion__heading-1")
    ANSWER_ACCORDION_2 = (By.XPATH, "//div[@id='accordion__panel-1']/p")
    QUESTION_ACCORDION_BUTTONS_3 = (By.ID, "accordion__heading-2")
    ANSWER_ACCORDION_3 = (By.XPATH, "//div[@id='accordion__panel-2']/p")
    QUESTION_ACCORDION_BUTTONS_4 = (By.ID, "accordion__heading-3")
    ANSWER_ACCORDION_4 = (By.XPATH, "//div[@id='accordion__panel-3']/p")
    QUESTION_ACCORDION_BUTTONS_5 = (By.ID, "accordion__heading-4")
    ANSWER_ACCORDION_5 = (By.XPATH, "//div[@id='accordion__panel-4']/p")
    QUESTION_ACCORDION_BUTTONS_6 = (By.ID, "accordion__heading-5")
    ANSWER_ACCORDION_6 = (By.XPATH, "//div[@id='accordion__panel-5']/p")
    QUESTION_ACCORDION_BUTTONS_7 = (By.ID, "accordion__heading-6")
    ANSWER_ACCORDION_7 = (By.XPATH, "//div[@id='accordion__panel-6']/p")
    QUESTION_ACCORDION_BUTTONS_8 = (By.ID, "accordion__heading-7")
    ANSWER_ACCORDION_8 = (By.XPATH, "//div[@id='accordion__panel-7']/p")

    BLOCK_WITH_QUESTIONS = (By.XPATH, "//div[contains(text(),'Вопросы о важном')]")
