from pages.practice_form_page.practice_form_page import PracticeFormPage


def test_fill_form(driver):
    driver.get("https://demoqa.com/automation-practice-form")
    form_page = PracticeFormPage(driver)

    form_page.fill_practice_form(
        first_name="Ahmet",
        last_name="Yılmaz",
        user_email="ahmet.yilmaz@example.com",
        phone_no="5551234567",
        date="10 May 1990",
        subjects="Maths",
        address="İstanbul, Türkiye"
    )

    modal_title = driver.find_element("id", "example-modal-sizes-title-lg").text
    assert modal_title == "Thanks for submitting the form"


def take_screenshot(driver, test_name):
    driver.save_screenshot(f"screenshots/{test_name}.png")
