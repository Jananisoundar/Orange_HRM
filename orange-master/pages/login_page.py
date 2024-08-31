# Import necessary modules from Selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        # Initialize the LoginPage with a WebDriver instance
        self.driver = driver
        # Define locators for the username field, password field, login button, and error message
        self.username_field = (By.NAME, "username")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[@type="submit"]')
        self.error_message = (By.CSS_SELECTOR, '.error-message')

    # Method to enter the username into the username field
    def enter_username(self, username):
        # Wait until the username field is visible, then send the username
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    # Method to enter the password into the password field
    def enter_password(self, password):
        # Wait until the password field is visible, then send the password
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    # Method to click the login button
    def click_login(self):
        # Wait until the login button is clickable, then click it
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.login_button)).click()

    # Method to perform the login action by entering the username and password, then clicking login
    def login(self, username, password):
        # Enter the username and password, then click login
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Method to check if login was successful
    def is_login_successful(self):
        # Assuming that the absence of an error message means login is successful
        return not WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.error_message)).is_displayed()
