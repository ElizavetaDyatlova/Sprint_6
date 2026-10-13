import allure

from pages.main_page import MainPage


@allure.feature("Навигация по логотипам")
class TestLogos:

    @allure.title("Клик по логотипу «Самокат» ведёт на главную")
    def test_logo_scooter_goes_to_main(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.wait_for_load()
        main_page.click_logo_scooter()
        assert main_page.check_url_is_main()

    @allure.title("Клик по логотипу «Яндекс» открывает Дзен в новой вкладке")
    def test_logo_yandex_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.open_main()
        main_page.wait_for_load()
        main_page.click_logo_yandex_and_switch()
        assert main_page.check_dzen_opened()