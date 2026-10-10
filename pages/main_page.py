import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть главную страницу")
    def open(self):
        self.driver.get(BASE_URL)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load(self):
        first_question = "Сколько это стоит? И как оплатить?"
        locator = self._build(MainPageLocators.QUESTION_ARROW, first_question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Кликнуть по вопросу «{question}»")
    def click_question_arrow(self, question):
        locator = self._build(MainPageLocators.QUESTION_ARROW, question)
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Дождаться раскрытия ответа")
    def wait_for_answer(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Получить текст ответа")
    def get_answer_text(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        return self.driver.find_element(*locator).text

    @allure.step("Кликнуть по верхней кнопке «Заказать»")
    def click_order_button_top(self):
        self.driver.find_element(*MainPageLocators.BUTTON_ORDER_TOP).click()

    @allure.step("Кликнуть по нижней кнопке «Заказать»")
    def click_order_button_bottom(self):
        element = self.driver.find_element(*MainPageLocators.BUTTON_ORDER_BOTTOM)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Кликнуть по логотипу «Самокат»")
    def click_logo_scooter(self):
        self.driver.find_element(*MainPageLocators.LOGO_SCOOTER).click()

    @allure.step("Кликнуть по логотипу «Яндекс»")
    def click_logo_yandex(self):
        self.driver.find_element(*MainPageLocators.LOGO_YANDEX).click()

    @staticmethod
    def _build(locator, question):
        return locator[0], locator[1].format(question=question)