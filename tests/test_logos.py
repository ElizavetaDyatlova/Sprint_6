import allure
from selenium.webdriver.support.wait import WebDriverWait

from pages.main_page import MainPage


@allure.feature("Навигация по логотипам")
class TestLogos:

    @allure.title("Клик по логотипу «Самокат» ведёт на главную")
    def test_logo_scooter_goes_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_for_load()
        main_page.click_logo_scooter()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    @allure.title("Клик по логотипу «Яндекс» открывает Дзен в новой вкладке")
    def test_logo_yandex_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.wait_for_load()

        original_handles = driver.window_handles
        main_page.click_logo_yandex()

        WebDriverWait(driver, 5).until(
            lambda d: len(d.window_handles) > len(original_handles)
        )
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 5).until(
            lambda d: "dzen.ru" in d.current_url or "yandex.ru" in d.current_url
        )
        assert "dzen.ru" in driver.current_url or "yandex.ru" in driver.current_url