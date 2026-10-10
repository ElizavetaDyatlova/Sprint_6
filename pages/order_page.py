from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.order_page_locators import OrderPageLocators


class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_first_step(self, name, surname, address, metro, phone):
        self.driver.find_element(*OrderPageLocators.INPUT_NAME).send_keys(name)
        self.driver.find_element(*OrderPageLocators.INPUT_SURNAME).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.INPUT_ADDRESS).send_keys(address)
        self._select_metro(metro)
        self.driver.find_element(*OrderPageLocators.INPUT_PHONE).send_keys(phone)

    def _select_metro(self, metro):
        field = self.driver.find_element(*OrderPageLocators.INPUT_METRO)
        field.click()
        field.send_keys(metro)
        option_locator = (
            OrderPageLocators.METRO_OPTION[0],
            OrderPageLocators.METRO_OPTION[1].format(station=metro),
        )
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(option_locator)
        ).click()

    def click_next(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_NEXT).click()

    def fill_second_step(self, date, rental_period, color, comment=""):
        date_field = self.driver.find_element(*OrderPageLocators.INPUT_DATE)
        date_field.send_keys(date)
        date_field.send_keys(Keys.ESCAPE)

        self.driver.find_element(*OrderPageLocators.DROPDOWN_RENTAL_PERIOD).click()
        period_locator = (
            OrderPageLocators.RENTAL_PERIOD_OPTION[0],
            OrderPageLocators.RENTAL_PERIOD_OPTION[1].format(period=rental_period),
        )
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(period_locator)
        ).click()

        if color == "black":
            self.driver.find_element(*OrderPageLocators.CHECKBOX_BLACK_LABEL).click()
        elif color == "grey":
            self.driver.find_element(*OrderPageLocators.CHECKBOX_GREY_LABEL).click()

        if comment:
            self.driver.find_element(*OrderPageLocators.INPUT_COMMENT).send_keys(comment)

    def click_order(self):
        self.driver.find_element(*OrderPageLocators.BUTTON_ORDER).click()

    def confirm_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(OrderPageLocators.BUTTON_CONFIRM_YES)
        ).click()

    def wait_for_success_modal(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(
                OrderPageLocators.MODAL_SUCCESS_TITLE
            )
        )

    def get_success_modal_text(self):
        return self.driver.find_element(*OrderPageLocators.MODAL_SUCCESS_TITLE).text