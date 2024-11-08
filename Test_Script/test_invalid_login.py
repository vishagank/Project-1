import pytest
from Page_object_model.Invalid_login import InvalidLoginPage


@pytest.mark.usefixtures("setup")
class TestInvalidLogin:

    def test_validate_invalid_login(self):
        # Create an instance of the InvalidLoginPage class
        invalid_login = InvalidLoginPage(self.driver)

        # Attempt to login with invalid credentials
        # Username: "Admin", Password: "hrsytr"
        invalid_login.Validating_Invalid_Login("Admin", "hrsytr")
