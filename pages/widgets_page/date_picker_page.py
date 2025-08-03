from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class DatePickerPage:
    def __init__(self, driver):
        self.driver = driver
        self.DATE_INPUT = (By.ID, "datePickerMonthYearInput")

    def select_date(self, date_string):
        date_input = self.driver.find_element(*self.DATE_INPUT)

        # Clear önce: Eğer önceden yazılmış bir tarih varsa, siliniyor
        date_input.clear()

        # Yeni tarih giriliyor
        date_input.send_keys(date_string)  # örnek: "05/10/2025"
        date_input.send_keys(Keys.ENTER)

    def get_selected_date(self):
        return self.driver.find_element(*self.DATE_INPUT).get_attribute("value")
