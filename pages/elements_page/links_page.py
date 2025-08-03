from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LinksPage:
    def __init__(self, driver):
        self.driver = driver
        self.link_response = (By.ID, "linkResponse")

    def click_link_by_text(self, link_text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, link_text))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, link_text)))
        element.click()
    def get_response_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.link_response)
        ).text
