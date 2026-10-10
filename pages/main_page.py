from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def wait_for_load(self):
        first_question = "Сколько это стоит? И как оплатить?"
        locator = self._build(MainPageLocators.QUESTION_ARROW, first_question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def click_question_arrow(self, question):
        locator = self._build(MainPageLocators.QUESTION_ARROW, question)
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_answer(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def get_answer_text(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        return self.driver.find_element(*locator).text

    #Заказ самоката
    def click_order_button_top(self):
        """Верхняя кнопка «Заказать» в шапке"""
        self.driver.find_element(*MainPageLocators.BUTTON_ORDER_TOP).click()

    def click_order_button_bottom(self):
        """Нижняя кнопка «Заказать» со скроллом до неё"""
        element = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_BOTTOM)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    #Логотипы
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    @staticmethod
    def _build(locator, question):
        return locator[0], locator[1].format(question=question)