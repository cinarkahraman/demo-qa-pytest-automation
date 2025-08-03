from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WebTablesPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_btn = (By.ID, "addNewRecordButton")
        self.firstName = (By.ID, "firstName")
        self.lastName = (By.ID, "lastName")
        self.userEmail = (By.ID, "userEmail")
        self.age = (By.ID, "age")
        self.salary = (By.ID, "salary")
        self.department = (By.ID, "department")
        self.submit_btn = (By.ID, "submit")
        self.search_input = (By.ID, "searchBox")
        self.table_rows = (By.XPATH, "//div[@class='rt-tbody']/div")

    def add_record(self):
        self.driver.find_element(*self.add_btn).click()

    def registration_form(self, name, surname, email, your_age, your_salary, your_department):
        self.driver.find_element(*self.firstName).send_keys(name)
        self.driver.find_element(*self.lastName).send_keys(surname)
        self.driver.find_element(*self.userEmail).send_keys(email)
        self.driver.find_element(*self.age).send_keys(your_age)
        self.driver.find_element(*self.salary).send_keys(your_salary)
        self.driver.find_element(*self.department).send_keys(your_department)
        self.driver.find_element(*self.submit_btn).click()

    def search_and_verify_record(self, search_term):
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(search_term)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        return self.verify_record_in_table(search_term, "")

    def verify_record_in_table(self, first_name, last_name):
        rows = self.driver.find_elements(*self.table_rows)
        for row in rows:
            if first_name in row.text and last_name in row.text:
                return True
        return False

    def click_edit_button(self):
        # İlk satırdaki düzenle butonuna tıkla (her kaydın başında varsayalım)
        edit_btn = self.driver.find_element(By.CSS_SELECTOR, "span[title='Edit']")
        edit_btn.click()

    def update_age(self, new_age):
        age_input = self.driver.find_element(*self.age)
        age_input.clear()
        age_input.send_keys(new_age)
        self.driver.find_element(*self.submit_btn).click()

    def click_delete_button(self):
        delete_btn = self.driver.find_element(By.CSS_SELECTOR, "span[title='Delete']")
        delete_btn.click()

    def is_record_deleted(self, search_term):
        self.driver.find_element(*self.search_input).clear()
        self.driver.find_element(*self.search_input).send_keys(search_term)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.table_rows)
        )
        rows = self.driver.find_elements(*self.table_rows)
        return all(search_term not in row.text for row in rows)
