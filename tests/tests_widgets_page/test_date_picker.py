import pytest

from pages.widgets_page.date_picker_page import DatePickerPage


def test_date_selection(driver):
    driver.get("https://demoqa.com/date-picker")
    date_picker = DatePickerPage(driver)

    target_date = "05/10/2025"
    date_picker.select_date(target_date)

    # Test sonrası: Seçilen tarihi doğrulama
    selected_date = date_picker.get_selected_date()
    assert selected_date == target_date, f"Tarih eşleşmedi: {selected_date} != {target_date}"