import pytest
from selenium import webdriver
import os
import time

# Directory where screenshots will be saved in case of test failures
SCREENSHOT_DIR = 'screenshots'


@pytest.fixture(scope="function")
def setup(request):
    """
    Fixture to initialize the WebDriver, open the test URL, and maximize the browser window.

    Args:
        request (pytest.FixtureRequest): The request object that allows access to the test context.

    Yields:
        webdriver.Chrome: The WebDriver instance used for the test.
    """
    # Initialize the WebDriver (Chrome in this case; you can use Firefox or others if needed)
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.

    # Open the login page of the test application
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Maximize the browser window
    driver.maximize_window()

    # Make the WebDriver instance accessible in the test class
    request.cls.driver = driver

    # Yield control back to the test
    yield driver

    # Quit the WebDriver after the test is completed
    driver.quit()


def pytest_runtest_makereport(item, call):
    """
    Hook function to capture a screenshot when a test fails.

    Args:
        item (pytest.Item): The pytest item (test function) being executed.
        call (pytest.CallInfo): Information about the call to the test function.
    """
    # Check if the test function execution has failed
    if call.when == 'call' and call.excinfo is not None:
        # Create the screenshots directory if it does not exist
        if not os.path.exists(SCREENSHOT_DIR):
            os.makedirs(SCREENSHOT_DIR)

        # Attempt to capture a screenshot
        driver = item.funcargs.get('setup', None)  # Retrieve the WebDriver instance from the fixture
        if driver:
            # Generate a timestamp for the screenshot file name
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(SCREENSHOT_DIR, f"screenshot-{timestamp}.png")

            # Save the screenshot to the specified path
            driver.save_screenshot(screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")
        else:
            print("Driver instance not found.")
