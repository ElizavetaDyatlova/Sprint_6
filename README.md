# Проект автоматизации тестирования Яндекс.Самокат

Основа для написания автотестов — фреймворк pytest и библиотека Selenium WebDriver.
Отчёты формируются в Allure.

## Установка

1. Установить зависимости:
   pip install -r requirements.txt

2. Установить браузер Mozilla Firefox.

## Запуск

1. Прогнать тесты с записью результатов в Allure:
   pytest --alluredir=allure_results

2. Открыть отчёт в браузере:
   allure serve allure_results

## Структура проекта

- tests/ - тесты, сгруппированные по функциональности.
- pages/ - Page Object классы для страниц.
- locators/ - локаторы элементов.
- allure_results/ - JSON-отчёты Allure.
- conftest.py - фикстуры.
- requirements.txt - внешние зависимости.