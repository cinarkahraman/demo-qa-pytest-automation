import time

from pages.elements_page.web_tables_page import WebTablesPage


def test_edit_and_delete_web_table_record(driver):
    driver.get("https://demoqa.com/webtables")
    page = WebTablesPage(driver)

    # Kayıt ekle
    page.add_record()
    page.registration_form("Çınar", "Kahraman", "example@mail.com", "23", "300000", "QA Test")
    time.sleep(2)
    # Kaydın eklenip eklenmediğini kontrol et
    assert page.verify_record_in_table("Çınar", "Kahraman")
    time.sleep(2)
    # Arama yap
    assert page.search_and_verify_record("Çınar")
    time.sleep(2)
    # Edit işlemi
    page.click_edit_button()
    time.sleep(2)
    page.update_age("30")
    time.sleep(2)
    # Güncelleme sonrası tekrar kontrol (yaşı doğrudan doğrulamak istiyorsan daha özel logic gerekir)
    assert page.search_and_verify_record("Çınar")
    time.sleep(2)
    # Silme işlemi
    page.click_delete_button()
    time.sleep(2)
    # Silindiğini doğrula
    assert page.is_record_deleted("Çınar")
