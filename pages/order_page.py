import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Заполнить шаг 1 «Для кого самокат»")
    def fill_first_step(self, name, surname, address, metro, phone):
        self.find(OrderPageLocators.INPUT_NAME).send_keys(name)
        self.find(OrderPageLocators.INPUT_SURNAME).send_keys(surname)
        self.find(OrderPageLocators.INPUT_ADDRESS).send_keys(address)
        self._select_metro(metro)
        self.find(OrderPageLocators.INPUT_PHONE).send_keys(phone)

    @allure.step("Выбрать станцию метро «{metro}»")
    def _select_metro(self, metro):
        field = self.find(OrderPageLocators.INPUT_METRO)
        field.click()
        field.send_keys(metro)
        option_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(station=metro),
        )
        self.wait_clickable(option_locator).click()

    @allure.step("Нажать «Далее»")
    def click_next(self):
        self.find(OrderPageLocators.BUTTON_NEXT).click()

    @allure.step("Заполнить шаг 2 «Про аренду»")
    def fill_second_step(self, date, rental_period, color, comment=""):
        date_field = self.find(OrderPageLocators.INPUT_DATE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)

        self.find(OrderPageLocators.DROPDOWN_RENTAL_PERIOD).click()
        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period=rental_period),
        )
        self.wait_clickable(period_locator).click()

        if color == "black":
            self.find(OrderPageLocators.CHECKBOX_BLACK_LABEL).click()
        elif color == "grey":
            self.find(OrderPageLocators.CHECKBOX_GREY_LABEL).click()

        if comment:
            self.find(OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    @allure.step("Нажать «Заказать» на шаге 2")
    def click_order(self):
        self.find(OrderPageLocators.BUTTON_ORDER).click()

    @allure.step("Подтвердить заказ кнопкой «Да»")
    def confirm_order(self):
        self.wait_clickable(OrderPageLocators.BUTTON_CONFIRM_YES).click()

    @allure.step("Дождаться окна «Заказ оформлен»")
    def wait_for_success_modal(self):
        self.wait_visible(OrderPageLocators.MODAL_SUCCESS_TITLE)

    @allure.step("Получить текст окна")
    def get_success_modal_text(self):
        return self.find(OrderPageLocators.MODAL_SUCCESS_TITLE).text