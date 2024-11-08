from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object_model.base_page import BasePage


class DeleteEmployee(BasePage):
    # Locators for elements on the page
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    PIM = (By.XPATH, "//span[text()='PIM']")
    CHECK_BOX = (By.XPATH, "(//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon'])[2]")
    DELETE_EMPLOYEE = (By.XPATH, "(//i[@class = 'oxd-icon bi-trash'])[1]")
    YES_DELETE = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    RECORDS = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")

    def login(self, username, password):
        """Log in to the application."""
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        print("Logged in successfully")

    def navigate_to_pim(self):
        """Navigate to the PIM section."""
        self.click_element(self.PIM)
        print("Navigated to PIM section")

    def select_employee_record(self):
        """Select the employee record."""
        self.scroll_to_element(self.RECORDS)
        self.verify_element_present(self.CHECK_BOX)
        self.click_element(self.CHECK_BOX)
        print("Employee record selected")

    def delete_employee(self):
        """Click on the delete button and confirm deletion."""
        self.click_element(self.DELETE_EMPLOYEE)
        self.verify_element_present(self.YES_DELETE)
        self.click_element(self.YES_DELETE)
        print("Employee deleted successfully")
