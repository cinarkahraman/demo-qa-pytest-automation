from selenium.webdriver.common.by import By


class TextBoxPage:
    def __init__(self, driver):
        self.driver = driver
        self.full_name = (By.ID, "userName")
        self.email = (By.ID, "userEmail")
        self.current_address = (By.ID, "currentAddress")
        self.permanent_address = (By.ID, "permanentAddress")
        self.submit_button = (By.ID, "submit")
        self.output_name = (By.ID, "name")
        self.output_email = (By.ID, "email")

    def fill_form(self, name, email, current_address, permanent_address):
        self.driver.find_element(*self.full_name).send_keys(name)
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.current_address).send_keys(current_address)
        self.driver.find_element(*self.permanent_address).send_keys(permanent_address)

        submit = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()

    def get_output(self):
        return {
            "name": self.driver.find_element(*self.output_name).text,
            "email": self.driver.find_element(*self.output_email).text
        }
