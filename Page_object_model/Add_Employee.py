from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException  # Add this line
from Page_object_model.base_page import BasePage


class AddEmployee(BasePage):
    # Locator definitions
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    PIM = (By.XPATH, "//span[text()='PIM']")
    ADD = (By.XPATH, "//button[normalize-space()='Add']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='First Name']")
    MIDDLE_NAME = (By.XPATH, "//input[@placeholder='Middle Name']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Last Name']")
    EMPLOYEE_ID = (By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    CREATE_LOGIN_DETAILS_TOGGLE = (By.XPATH, "//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
    USERNAME = (By.XPATH, "(//input[@class = 'oxd-input oxd-input--active'])[3]")
    PASSWORD_TXT = (By.XPATH, "(//input[@type='password'])[1]")
    CONFIRM_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    SAVE = (By.XPATH, "//button[normalize-space()='Save']")
    PERSONAL_DETAILS_LABELS = (By.XPATH, "//h6[text()='Personal Details']")
    DRIVER_LICENSE_NUMBER = (By.XPATH, "(//input[@class = 'oxd-input oxd-input--active'])[4]")
    GENDER_LABEL = (By.XPATH,"//label[normalize-space()='Gender']")
    MALE_GENDER = (By.XPATH, "//input[@value='1']")
    PERSONAL_INFO_SAVE_BUTTON = (By.XPATH,"(//button[@type='submit'][normalize-space()='Save'])[1]")

    def login(self, username, password):
        """Logs into the application using the provided username and password."""
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BUTTON)

    def navigate_to_add_employee(self):
        """Navigates to the Add Employee section."""
        self.click_element(self.PIM)
        self.click_element(self.ADD)

    def enter_employee_details(self, first_name, middle_name, last_name, emp_id):
        """Enters the basic employee details like first name, middle name, last name, and employee ID."""
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.MIDDLE_NAME, middle_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.EMPLOYEE_ID, emp_id)

    def toggle_create_login_details(self):
        """Toggles the switch to create login details for the new employee."""
        self.click_element(self.CREATE_LOGIN_DETAILS_TOGGLE)

    def enter_login_details(self, user_name, psw, confirm_psw):
        """Enters the login details for the new employee."""
        self.scroll_to_bottom()
        self.enter_text(self.USERNAME, user_name)
        self.enter_text(self.PASSWORD_TXT, psw)
        self.enter_text(self.CONFIRM_PASSWORD, confirm_psw)

    def save_new_employee(self):
        """Clicks the save button to add the new employee."""
        self.click_element(self.SAVE)

    def add_additional_details(self, license_num):
        """Enters additional details like driver's license number and selects gender."""
        # Wait for the Personal Details label to be visible and clickable
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PERSONAL_DETAILS_LABELS))
        self.scroll_to_element(self.PERSONAL_DETAILS_LABELS)  # Scroll to the personal details section
        self.verify_element_visible(self.DRIVER_LICENSE_NUMBER)

        # Scroll to the license input field to ensure it's in view
        self.scroll_to_element(self.DRIVER_LICENSE_NUMBER)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.DRIVER_LICENSE_NUMBER))

        # Clear any existing text and enter the license number
        self.clear_and_enter_text_if_value_exists(self.DRIVER_LICENSE_NUMBER, license_num)

        # Scroll to gender label and select gender
        self.verify_element_visible(self.GENDER_LABEL)
        self.scroll_to_element(self.GENDER_LABEL)

        # Ensure the gender radio button is clickable and click it
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.MALE_GENDER))
            self.click_element(self.MALE_GENDER)
        except ElementClickInterceptedException:
            # If click is intercepted, use JavaScript to click on the radio button
            self.driver.execute_script("arguments[0].click();", self.find_element(self.MALE_GENDER))
        except Exception as e:
            print(f"Error clicking gender radio button: {e}")
            # Attempt to click using JavaScript as a last resort
            self.driver.execute_script("arguments[0].click();", self.find_element(self.MALE_GENDER))

        # Save the personal information
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.PERSONAL_INFO_SAVE_BUTTON))
        self.click_element(self.PERSONAL_INFO_SAVE_BUTTON)