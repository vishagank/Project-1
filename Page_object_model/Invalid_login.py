from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object_model.base_page import BasePage


class InvalidLoginPage(BasePage):
    # Locators for elements on the login page
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    ERROR_MESSAGE = (By.XPATH, "//p[text()='Invalid credentials']")

    def Validating_Invalid_Login(self, username, password):
        # Attempt to log in with invalid credentials

        # Enter the username in the username field
        self.enter_text(self.USER_NAME, username)

        # Enter the password in the password field
        self.enter_text(self.PASSWORD, password)

        # Click the login button to submit the form
        self.click_element(self.LOGIN_BUTTON)

        # Wait until the error message is visible
        message_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )

        # Get the text of the error message
        actual_message = message_element.text

        # Define the expected error message
        expected_message = "Invalid credentials"

        # Validate that the actual error message matches the expected message
        assert actual_message == expected_message, f"Expected '{expected_message}', but got '{actual_message}'"
