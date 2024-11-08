from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Page_object_model.base_page import BasePage


class LoginPage(BasePage):
    # Locators for elements on the login page
    USER_NAME = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    PIM = (By.XPATH, "//span[text()='PIM']")

    def Login_Orange_HRM_Successfully(self, username, password):
        # Logs into the Orange HRM application using provided username and password

        # Enter the username in the username field
        self.enter_text(self.USER_NAME, username)

        # Enter the password in the password field
        self.enter_text(self.PASSWORD, password)

        # Click the login button to submit the form
        self.click_element(self.LOGIN_BUTTON)

        try:
            # Wait until the PIM element is visible to confirm successful login
            pim_element = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.PIM)
            )
            # Print the text of the PIM element for verification
            print(f"PIM Element Text: {pim_element.text}")
        except Exception as e:
            # Log the error if the PIM element is not found
            print(f"Error finding PIM element: {e}")
