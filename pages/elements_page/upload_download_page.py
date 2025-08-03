from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


class UploadDownloadPage:
    def __init__(self, driver):
        self.driver = driver
        self.upload_input = (By.ID, "uploadFile")
        self.upload_message = (By.ID, "uploadedFilePath")
        self.download_link = (By.ID, "downloadButton")

    def upload_file(self, file_path):
        """Dosya yükleme işlemi."""
        upload_element = self.driver.find_element(*self.upload_input)
        upload_element.send_keys(file_path)  # Dosya yolunu gönder
        time.sleep(2)  # Yüklemenin tamamlanması için biraz bekleyelim

    def get_uploaded_file_message(self):
        """Yüklenen dosyanın mesajını al."""
        return self.driver.find_element(*self.upload_message).text

    def download_file(self):
        """Dosya indirme işlemi."""
        download_element = self.driver.find_element(*self.download_link)
        download_element.click()
        time.sleep(2)  # İndirme işlemi için biraz bekleyelim
