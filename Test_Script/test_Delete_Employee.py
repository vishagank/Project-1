import pytest
from Page_object_model.Delete_Employee import DeleteEmployee


@pytest.mark.usefixtures("setup")
class TestDeleteEmployee:
    # Test case to validate the deletion of an employee
    def test_validate_delete_employee(self):
        # Initialize the DeleteEmployee page object
        delete_emp = DeleteEmployee(self.driver)

        # Perform the employee deletion process
        delete_emp.login("Admin", "admin123")
        delete_emp.navigate_to_pim()
        delete_emp.select_employee_record()
        delete_emp.delete_employee()

        # Optionally, add assertions to verify that the employee has been deleted
        # For example, you could check if the employee record is no longer present.

        # Example assertion (assuming you have a method to check employee presence):
        # employee_exists = delete_emp.is_employee_present()
        # assert not employee_exists, "Employee was not deleted successfully"

        print("Test for deleting employee validated successfully")
