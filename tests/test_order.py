import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage

ORDER_DATA = [
    {
        "entry": "top",
        "name": "Иван",
        "surname": "Иванов",
        "address": "Москва, ул. Ленина, 1",
        "metro": "Черкизовская",
        "phone": "+79991234567",
        "date": "15.11.2026",
        "rental_period": "сутки",
        "color": "black",
        "comment": "-",
    },
    {
        "entry": "bottom",
        "name": "Пётр",
        "surname": "Петров",
        "address": "Санкт-Петербург, Невский пр., 10",
        "metro": "Сокольники",
        "phone": "+79997654321",
        "date": "20.11.2026",
        "rental_period": "двое суток",
        "color": "grey",
        "comment": "",
    },
]


@allure.feature("Заказ самоката")
class TestOrder:

    @allure.title("Успешный заказ через {data[entry]} кнопку")
    @pytest.mark.parametrize("data", ORDER_DATA)
    def test_order_scooter_success(self, driver, data):
        main_page = MainPage(driver)
        main_page.open_main()

        if data["entry"] == "top":
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()

        order_page = OrderPage(driver)
        order_page.fill_first_step(
            data["name"], data["surname"], data["address"], data["metro"], data["phone"]
        )
        order_page.click_next()
        order_page.fill_second_step(
            data["date"], data["rental_period"], data["color"], data["comment"]
        )
        order_page.click_order()
        order_page.confirm_order()
        order_page.wait_for_success_modal()

        assert "Заказ оформлен" in order_page.get_success_modal_text()
