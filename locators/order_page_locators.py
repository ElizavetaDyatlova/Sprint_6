from selenium.webdriver.common.by import By


class OrderPageLocators:
  
    INPUT_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, "//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, "//button[text()='Далее']")

    METRO_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'select-search__select')]//div[text()='{station}']"
    )

    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    DROPDOWN_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-root")
    RENTAL_PERIOD_OPTION = (
        By.XPATH,
        "//div[contains(@class, 'Dropdown-option') and text()='{period}']"
    )
    CHECKBOX_BLACK_LABEL = (By.XPATH, "//label[@for='black']")
    CHECKBOX_GREY_LABEL = (By.XPATH, "//label[@for='grey']")
    INPUT_COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons__1xGrp')]/button[text()='Заказать']"
    )

    BUTTON_CONFIRM_YES = (By.XPATH, "//button[text()='Да']")
    MODAL_SUCCESS_TITLE = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']"
    )