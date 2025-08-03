from pages.elements_page.checkbox_page import CheckBoxPage
import time


def test_checkbox_selection(driver):
    driver.get("https://demoqa.com/checkbox")
    page = CheckBoxPage(driver)

    # Tüm checkbox ağacını açıyoruz
    page.expand_home()

    # Farklı checkbox'ları seçiyoruz
    page.select_checkbox(page.desktop_checkbox)
    page.select_checkbox(page.documents_checkbox)
    page.select_checkbox(page.downloads_checkbox)

    # Sonuçları kontrol ediyoruz
    result = page.get_result()
    assert "desktop" in result.lower()
    assert "documents" in result.lower()
    assert "downloads" in result.lower()
    # tree-node > ol > li > span > label > span.rct-checkbox > svg

    time.sleep(3)  # Sonuçları gözlemleyebilmek için bekleme
