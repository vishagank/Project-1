from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def verify_element_present(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return element.is_displayed()

    def scroll_to_element(self, locator, timeout=10):
        """Scrolls the page until the element is in view"""
        element = self.find_element(locator, timeout)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)

    def scroll_to_bottom(self):
        """Scrolls to the bottom of the page"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        """Scrolls to the top of the page"""
        self.driver.execute_script("window.scrollTo(0, 0);")

    def scroll_by_offset(self, x_offset=0, y_offset=0):
        """Scrolls by the specified x and y offset"""
        self.driver.execute_script(f"window.scrollBy({x_offset}, {y_offset});")

    def select_dropdown_by_visible_text(self, locator, visible_text, timeout=10):
        """Selects a dropdown option by visible text"""
        element = self.find_element(locator, timeout)
        select = Select(element)
        select.select_by_visible_text(visible_text)

    def select_dropdown_by_value(self, locator, value, timeout=10):
        """Selects a dropdown option by its value"""
        element = self.find_element(locator, timeout)
        select = Select(element)
        select.select_by_value(value)

    def select_dropdown_by_index(self, locator, index, timeout=10):
        """Selects a dropdown option by its index"""
        element = self.find_element(locator, timeout)
        select = Select(element)
        select.select_by_index(index)

    def clear_and_enter_text_if_value_exists(self, locator, text, timeout=10):
        """Clears an input field if it already has a value, then enters new text."""
        element = self.find_element(locator, timeout)

        # Scroll to the element and bring it into view
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Wait for the element to be clickable
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

        try:
            # Click on the element to focus it
            element.click()
        except ElementClickInterceptedException:
            # If click is intercepted, use JavaScript to focus on it
            self.driver.execute_script("arguments[0].focus();", element)

        # Get the current value of the input field
        existing_value = element.get_attribute("value")

        if existing_value:
            print(f"Clearing existing value: {existing_value}")
            # Clear the field using both clear() and JavaScript to ensure it's cleared
            element.clear()
            self.driver.execute_script("arguments[0].value = '';", element)

        # After clearing, enter the new text
        element.send_keys(text)
        print(f"Entered new text: {text}")

    def verify_element_visible(self, locator, timeout=10):
        """Verifies if the element is visible on the page."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def upload_file(self, locator, file_path, timeout=10):
        """Uploads a file by sending the file path to the input element."""
        file_input = self.find_element(locator, timeout)
        file_input.send_keys(file_path)