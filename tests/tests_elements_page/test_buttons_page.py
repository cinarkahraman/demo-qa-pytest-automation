from pages.elements_page.buttons_page import ButtonsPage


def test_button_page(driver):
    driver.get("https://demoqa.com/buttons")
    page = ButtonsPage(driver)
    assert "You have done a double click" in page.double_click_me()
    assert "You have done a right click" in page.right_click_me()
    assert "You have done a dynamic click" in page.single_click_me()

