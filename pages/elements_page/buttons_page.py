from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class ButtonsPage:
    def __init__(self, driver):
        self.driver = driver
        self.double_click_btn = (By.ID, "doubleClickBtn")
        self.right_click_btn = (By.ID, "rightClickBtn")
        self.single_click_btn = (By.XPATH, "//button[text()='Click Me']")  # ID dinamik olabiliyor
        self.double_msg = (By.ID, "doubleClickMessage")
        self.right_msg = (By.ID, "rightClickMessage")
        self.single_msg = (By.ID, "dynamicClickMessage")

    def double_click_me(self):
        btn = self.driver.find_element(*self.double_click_btn)
        ActionChains(self.driver).double_click(btn).perform()
        return self.driver.find_element(*self.double_msg).text

    def right_click_me(self):
        btn = self.driver.find_element(*self.right_click_btn)
        ActionChains(self.driver).context_click(btn).perform()
        return self.driver.find_element(*self.right_msg).text

    def single_click_me(self):
        self.driver.find_element(*self.single_click_btn).click()
        return self.driver.find_element(*self.single_msg).text
