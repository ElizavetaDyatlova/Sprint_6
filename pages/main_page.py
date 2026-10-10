from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Открыть главную страницу."""
        self.driver.get(BASE_URL)

    def wait_for_load(self):
        """Ждём появления первого вопроса выпадающего списка."""
        first_question = "Сколько это стоит? И как оплатить?"
        locator = self._build(MainPageLocators.QUESTION_ARROW, first_question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def click_question_arrow(self, question):
        """Кликнуть по стрелке вопроса.

        Прокручиваем элемент в центр экрана и кликаем через JavaScript —
        так обходим перекрытие соседними блоками после раскрытия ответа.
        """
        locator = self._build(MainPageLocators.QUESTION_ARROW, question)
        element = self.driver.find_element(*locator)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )
        self.driver.execute_script("arguments[0].click();", element)

    def wait_for_answer(self, question):
        """Ждём, пока раскроется ответ под вопросом."""
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    def get_answer_text(self, question):
        """Получить текст ответа."""
        locator = self._build(MainPageLocators.ANSWER_TEXT, question)
        return self.driver.find_element(*locator).text

    @staticmethod
    def _build(locator, question):
        """Подставить текст вопроса в шаблон локатора."""
        return locator[0], locator[1].format(question=question)