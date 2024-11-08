import pytest
from Page_object_model.successfull_login import LoginPage


@pytest.mark.usefixtures("setup")  # This decorator ensures that the setup fixture is used for the test class
class TestLogin:

    def test_validate_success_login(self):
        """
        Test case to validate successful login to the Orange HRM application.
        Steps:
        1. Initialize the login page object.
        2. Perform login using valid credentials.
        """
        # Initialize the LoginPage object
        login_page = LoginPage(self.driver)

        # Perform a successful login with valid username and password
        login_page.Login_Orange_HRM_Successfully("Admin", "admin123")
