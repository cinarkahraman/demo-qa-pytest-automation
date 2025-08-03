from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AlertsPage:
    def __init__(self, driver):
        self.driver = driver
        self.simple_alert_btn = (By.ID, "alertButton")
        self.timer_alert_btn = (By.ID, "timerAlertButton")
        self.confirm_alert_btn = (By.ID, "confirmButton")
        self.prompt_alert_btn = (By.ID, "promtButton")
        self.prompt_result = (By.ID, "promptResult")

    def click_simple_alert(self):
        self.driver.find_element(*self.simple_alert_btn).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    def click_timer_alert(self):
        self.driver.find_element(*self.timer_alert_btn).click()
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text

    def click_confirm_alert(self, accept=True):
        self.driver.find_element(*self.confirm_alert_btn).click()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        if accept:
            alert.accept()
        else:
            alert.dismiss()
        return alert_text

    def click_prompt_alert(self, input_text):
        self.driver.find_element(*self.prompt_alert_btn).click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(input_text)
        alert.accept()
        return alert.text

    def get_prompt_result(self):
        return self.driver.find_element(*self.prompt_result).text
