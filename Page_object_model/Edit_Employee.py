from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object_model.base_page import BasePage


class EditEmployee(BasePage):
    # Locators for elements on the page
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    PIM = (By.XPATH, "//span[text()='PIM']")
    CHECK_BOX = (By.XPATH, "(//i[@class = 'oxd-icon bi-check oxd-checkbox-input-icon'])[2]")
    EDIT_EMPLOYEE = (By.XPATH, "(//i[@class='oxd-icon bi-pencil-fill'])[10]")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'][normalize-space()='Sauvegarder'])[1]")
    EDIT_MIDDLE_NAME = (By.XPATH, "//input[@name = 'middleName']")
    RECORDS = (By.XPATH, "//span[@class='oxd-text oxd-text--span']")

    def login(self, username, password):
        """Login to the application."""
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)
        print("Logged in successfully")

    def navigate_to_pim(self):
        """Navigate to the PIM section."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.PIM))
        self.click_element(self.PIM)
        print("Navigated to PIM section")

    def select_employee_record(self):
        """Select the employee record."""
        self.scroll_to_element(self.RECORDS)
        self.verify_element_present(self.CHECK_BOX)
        self.click_element(self.CHECK_BOX)
        print("Employee record selected")

    def click_edit_employee(self):
        """Click on the edit button for the employee."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.EDIT_EMPLOYEE))
        self.click_element(self.EDIT_EMPLOYEE)
        print("Clicked on the edit employee button")

    def update_middle_name(self, middle_name):
        """Update the middle name of the employee."""
        self.verify_element_present(self.EDIT_MIDDLE_NAME)
        self.clear_and_enter_text_if_value_exists(self.EDIT_MIDDLE_NAME, middle_name)
        print(f"Updated middle name to {middle_name}")

    def save_changes(self):
        """Save the changes made to the employee details."""
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        self.click_element(self.SAVE_BUTTON)
        print("Details saved successfully")
