import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(BASE_URL)

    @allure.step("Дождаться загрузки главной страницы")
    def wait_for_load(self):
        first_question = "Сколько это стоит? И как оплатить?"
        locator = self._build(MainPageLocators.QUESTION_ARROW, first_question)
        self.wait_visible(locator)

    @allure.step("Кликнуть по вопросу «{question}»")
    def click_question_arrow(self, question):
        locator = self._build(MainPageLocators.QUESTION_ARROW, question)
        element = self.find(locator)
        self.scroll_to(element)
        self.js_click(element)

    @allure.step("Дождаться раскрытия ответа")
    def wait_for_answer(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        self.wait_visible(locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, question):
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        return self.find(locator).text

    @allure.step("Кликнуть по верхней кнопке «Заказать»")
    def click_order_button_top(self):
        self.find(MainPageLocators.BUTTON_ORDER_TOP).click()

    @allure.step("Кликнуть по нижней кнопке «Заказать»")
    def click_order_button_bottom(self):
        element = self.find(MainPageLocators.BUTTON_ORDER_BOTTOM)
        self.scroll_to(element)
        self.js_click(element)

    @allure.step("Кликнуть по логотипу «Самокат»")
    def click_logo_scooter(self):
        self.find(MainPageLocators.LOGO_SCOOTER).click()

    @allure.step("Кликнуть по логотипу «Яндекс»")
    def click_logo_yandex(self):
        self.find(MainPageLocators.LOGO_YANDEX).click()

    @staticmethod
    def _build(locator, question):
        return locator[0], locator[1].format(question=question)