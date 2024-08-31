# Import necessary modules for waiting and expected conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        # Initialize the BasePage with a WebDriver instance
        self.driver = driver

    # Method to find an element on the page, with an optional timeout
    def find_element(self, locator, timeout=10):
        # Wait until the element is located or until the timeout is reached
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    # Method to click an element on the page, with an optional timeout
    def click_element(self, locator, timeout=10):
        # Find the element first, then click it
        element = self.find_element(locator, timeout)
        element.click()

    # Method to enter text into a field, with an optional timeout
    def enter_text(self, locator, text, timeout=10):
        # Find the element, clear any existing text, then send the new text
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    # Method to get the current URL of the page
    def get_current_url(self):
        return self.driver.current_url
