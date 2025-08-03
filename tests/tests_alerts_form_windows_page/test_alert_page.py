import pytest

from pages.alerts_form_windows_page.alerts_page import AlertsPage


def test_simple_alert(driver):
    page = AlertsPage(driver)
    driver.get("https://demoqa.com/alerts")
    text = page.click_simple_alert()
    assert text == "You clicked a button"


def test_timer_alert(driver):
    page = AlertsPage(driver)
    driver.get("https://demoqa.com/alerts")
    text = page.click_timer_alert()
    assert text == "This alert appeared after 5 seconds"


def test_confirm_alert_accept(driver):
    page = AlertsPage(driver)
    driver.get("https://demoqa.com/alerts")
    text = page.click_confirm_alert(accept=True)
    assert text == "Do you confirm action?"


def test_confirm_alert_dismiss(driver):
    page = AlertsPage(driver)
    driver.get("https://demoqa.com/alerts")
    text = page.click_confirm_alert(accept=False)
    assert text == "Do you confirm action?"


def test_prompt_alert(driver):
    page = AlertsPage(driver)
    driver.get("https://demoqa.com/alerts")
    input_value = "TestUser"
    page.click_prompt_alert(input_value)
    result = page.get_prompt_result()
    assert input_value in result
