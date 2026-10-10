from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы Яндекс.Самоката."""

    #Стрелка выпадающего списка «Вопросы о важном».
    #Находится внутри кнопки с текстом вопроса. Клик по ней раскрывает ответ.
    QUESTION_ARROW = (
        By.XPATH,
        "//div[contains(@class, 'accordion__button') and text()='{question}']"
    )

    #Текст ответа под раскрытым вопросом.
    ANSWER_TEXT = (
        By.XPATH,
        "//div[contains(@class, 'accordion__item')]"
        "[.//div[contains(@class, 'accordion__button') and text()='{question}']]"
        "//div[contains(@class, 'accordion__panel')]"
    )