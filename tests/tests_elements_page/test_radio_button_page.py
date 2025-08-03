import time

from pages.elements_page.radiobutton_page import RadioButtonPage


def test_radio_buttons(driver):
    page = RadioButtonPage(driver)
    driver.get("https://demoqa.com")
    page.navigate_to_radio_button_section()
    time.sleep(3)
    result_yes = page.select_yes_radio_button()
    assert "Yes" in result_yes
    time.sleep(3)
    result_impressive = page.select_impressive_radio_button()
    assert "Impressive" in result_impressive
    time.sleep(3)