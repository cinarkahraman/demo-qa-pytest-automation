import time
import os

from pages.elements_page.upload_download_page import UploadDownloadPage


def test_upload_download_file(driver):
    driver.get("https://demoqa.com/upload-download")
    page = UploadDownloadPage(driver)

    # 1. Dosya Yükleme
    file_path = "../tests_practice_form_page/sample.txt"  # Yüklemek istediğiniz dosyanın yolu
    if os.path.exists(file_path):
        page.upload_file(file_path)
        uploaded_message = page.get_uploaded_file_message()
        assert "sample.txt" in uploaded_message, f"Yüklenen dosya mesajında 'sample.txt' bulunamadı. Mesaj: {uploaded_message}"
    else:
        print(f"❌ Dosya bulunamadı: {file_path}")
        return  # Dosya yoksa testi sonlandır

    # 2. Dosya İndirme
    page.download_file()

    # İndirme işlemi için biraz bekleyelim
    time.sleep(2)

    download_path = "./downloaded_files/"
    file_name = "sampleFile.jpeg"  # İndirilen dosyanın adı

    # İndirilmiş dosyanın var olup olmadığını kontrol et
    downloaded_file_path = os.path.join(download_path, file_name)
    assert os.path.exists(downloaded_file_path), f"İndirilen dosya bulunamadı. Beklenen dosya: {downloaded_file_path}"
