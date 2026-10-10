import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    """Открывает Firefox перед тестом и закрывает его после"""
    driver = webdriver.Firefox()
    yield driver
    driver.quit()