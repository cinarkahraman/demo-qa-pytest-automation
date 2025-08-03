import time

from pages.elements_page.text_box_page import TextBoxPage


def test_text_box_form(driver):
    driver.get("https://demoqa.com/text-box")
    page = TextBoxPage(driver)
    page.fill_form("Çınar Kahraman", "mail@example.com", "Ankara", "İstanbul")

    output = page.get_output()
    assert "Çınar Kahraman" in output["name"]
    assert "mail@example.com" in output["email"]
    time.sleep(5)