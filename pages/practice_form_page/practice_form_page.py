from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PracticeFormPage:
    def __init__(self, driver):
        self.driver = driver
        self.FIRST_NAME = (By.ID, "firstName")
        self.LAST_NAME = (By.ID, "lastName")
        self.USER_EMAIL = (By.ID, "userEmail")
        self.GENDER_LABEL = (By.XPATH, "//label[@for='gender-radio-1']")
        self.PHONE_NO = (By.ID, "userNumber")
        self.DATE = (By.ID, "dateOfBirthInput")
        self.SUBJECTS = (By.CSS_SELECTOR, "#subjectsInput")
        self.HOBBY_LABEL = (By.XPATH, "//label[@for='hobbies-checkbox-1']")
        self.UPLOAD_PIC = (By.ID, "uploadPicture")
        self.ADDRESS = (By.ID, "currentAddress")
        self.STATE = (By.CSS_SELECTOR, "#react-select-6-input")
        self.CITY = (By.CSS_SELECTOR, "#react-select-7-input")
        self.SUBMIT_BTN = (By.CSS_SELECTOR, "#submit")

    def fill_practice_form(self, first_name, last_name, user_email, phone_no, date, subjects, address):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.USER_EMAIL).send_keys(user_email)
        self.driver.find_element(*self.PHONE_NO).send_keys(phone_no)
        self.driver.find_element(*self.ADDRESS).send_keys(address)

        # Date picker
        date_input = self.driver.find_element(*self.DATE)
        date_input.clear()
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

        # Gender selection (label click)
        self.driver.find_element(*self.GENDER_LABEL).click()

        # Subject entry
        subject_input = self.driver.find_element(*self.SUBJECTS)
        subject_input.send_keys(subjects)
        subject_input.send_keys(Keys.ENTER)

        hobby_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@for='hobbies-checkbox-1']"))
        )
        hobby_label.click()

        # Wait for state input to be visible and interactable
        state_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-6-input"))
        )
        state_input.send_keys("NCR")
        state_input.send_keys(Keys.ENTER)

        # Wait for city input to be visible and interactable
        city_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-7-input"))
        )
        city_input.send_keys("Delhi")
        city_input.send_keys(Keys.ENTER)

        # Wait for the upload file input to be visible
        upload_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "uploadPicture"))
        )
        upload_input.send_keys("sample.txt")

        # Click the submit button
        submit_button = self.driver.find_element(*self.SUBMIT_BTN)
        submit_button.click()
