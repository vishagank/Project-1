import pytest
from Page_object_model.Add_Employee import AddEmployee


@pytest.mark.usefixtures("setup")
class TestAddEmployee:

    def test_validate_add_employee(self):
        # Create an instance of the AddEmployee page object
        add_emp = AddEmployee(self.driver)
        # Call the individual methods to add a new employee
        add_emp.login("Admin", "admin123")  # Log in with admin credentials
        add_emp.navigate_to_add_employee()  # Navigate to the Add Employee section
        add_emp.enter_employee_details("harsha", "giri", "jasna", "10001")  # Enter employee details
        add_emp.toggle_create_login_details()  # Toggle the switch to create login details
        add_emp.enter_login_details("harsha07", "Test@1234", "Test@1234")  # Enter login details for the new employee
        add_emp.save_new_employee()  # Save the new employee
        add_emp.add_additional_details("LIC1001")  # Enter additional details like license number
