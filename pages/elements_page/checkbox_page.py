from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class CheckBoxPage:
    def __init__(self, driver):
        self.driver = driver
        # Ana ağacı açma butonu
        self.home_toggle = (By.CSS_SELECTOR, ".rct-node:nth-child(1) .rct-collapse")

        # Checkbox'lar (Desktop, Documents, Downloads)
        self.desktop_checkbox = (By.XPATH, "//span[@class='rct-title' and text()='Desktop']")
        self.documents_checkbox = (By.XPATH, "//span[@class='rct-title' and text()='Documents']")
        self.downloads_checkbox = (By.XPATH, "//span[@class='rct-title' and text()='Downloads']")

        # Sonuç metni
        self.result_text = (By.ID, "result")

    def expand_home(self):
        """Ana ağacı açar."""
        self.driver.find_element(*self.home_toggle).click()

    def select_checkbox(self, checkbox):
        """Verilen checkbox'ı seçer."""
        element = self.driver.find_element(*checkbox)
        ActionChains(self.driver).move_to_element(element).perform()
        element.click()

    def get_result(self):
        """Sonuç metnini döndürür."""
        return self.driver.find_element(*self.result_text).text
    