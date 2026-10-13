import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть страницу {url}")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент по локатору")
    def find(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Найти все элементы по локатору")
    def find_all(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Дождаться видимости элемента")
    def wait_visible(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step("Дождаться кликабельности элемента")
    def wait_clickable(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step("Прокрутить страницу к элементу")
    def scroll_to(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", element
        )

    @allure.step("Кликнуть по элементу")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Получить список открытых вкладок")
    def get_window_handles(self):
        return self.driver.window_handles

    @allure.step("Переключиться на указанную вкладку")
    def switch_to_window(self, handle):
        self.driver.switch_to.window(handle)

    @allure.step("Дождаться появления новой вкладки")
    def wait_for_new_tab(self, original_handles, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )

    @allure.step("Дождаться, что URL содержит один из вариантов: {substrings}")
    def wait_for_url_contains_any(self, substrings, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            lambda d: any(s in d.current_url for s in substrings)
        )