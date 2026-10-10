from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы Яндекс.Самоката."""

    # --- Выпадающий список «Вопросы о важном» ---
    QUESTION_ARROW = (
        By.XPATH,
        "//div[contains(@class, 'accordion__button') and text()='{question}']"
    )
    ANSWER_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'accordion__item')]"
        "[.//div[contains(@class, 'accordion__button') and text()='{question}']]"
        "//div[contains(@class, 'accordion__panel')]"
    )

    # --- Кнопки «Заказать» ---
    BUTTON_ORDER_TOP = (
        By.XPATH,
        "//button[contains(@class, 'Button_Button__ra12g') "
        "and not(contains(@class, 'Button_UtralBig__uhLo7'))]"
    )
    BUTTON_ORDER_BOTTOM = (
    By.XPATH,
    "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']"
)

    # --- Логотипы ---
    LOGO_SCOOTER = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__3lsAR')]")
    LOGO_YANDEX = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex__3TSOI')]")