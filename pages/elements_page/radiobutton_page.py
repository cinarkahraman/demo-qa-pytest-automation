from selenium.webdriver.common.by import By


class RadioButtonPage:
    def __init__(self, driver):
        self.driver = driver
        self.elementsDropDownButton = (By.CSS_SELECTOR, ".card.mt-4.top-card")
        self.radioButtonPage = (By.XPATH, "//span[text()='Radio Button']")
        self.yesRadioLabel = (By.XPATH, "//label[@for='yesRadio']")
        self.impressiveRadioLabel = (By.XPATH, "//label[@for='impressiveRadio']")
        self.selectedRadioMsg = (By.CLASS_NAME, "mt-3")

    def navigate_to_radio_button_section(self):
        self.driver.find_element(*self.elementsDropDownButton).click()
        self.driver.find_element(*self.radioButtonPage).click()

    def select_yes_radio_button(self):
        self.driver.find_element(*self.yesRadioLabel).click()
        return self.driver.find_element(*self.selectedRadioMsg).text

    def select_impressive_radio_button(self):
        self.driver.find_element(*self.impressiveRadioLabel).click()
        return self.driver.find_element(*self.selectedRadioMsg).text

