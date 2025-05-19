from pages.base_page import BasePage
from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WaitUtils(driver, timeout=10)
        self.username_input = (By.XPATH, "//input[@name='name']")
        self.email_input = (By.XPATH, "//input[@data-qa='signup-email']")
        self.signup_btn = (By.XPATH, "//input[@data-qa='signup-button']")
        self.login_email = (By.XPATH, "//input[@data-qa='login-email']")
        self.login_pass = (By.XPATH, "//input[@data-qa='login-password']")
        self.login_btn = (By.XPATH, "//button[@data-qa='login-button']")
        self.submit_reg = (By.XPATH, "//button[@data-qa = 'signup-button']")
        self.home_heading = (By.XPATH, "//a[contains(text(), 'Home')]")
        self.verify_page = (By.XPATH, "//h2[contains(text(), 'New User Signup!')]")
        self.verify_submit_reg = (By.XPATH, "//b[contains(text(),'Enter Account Information')]")

    def check_loginpage_load(self):
        try:
            self.logger.info("Checking if Home page heading is displayed.")
            return self.wait.wait_for_element_to_be_visible(self.home_heading)
        except Exception as e:
            self.logger.error(f"Error loading homepage: {e}")
            return False

    def enter_username(self, login_mail):
        self.logger.info(f"Entering login email: {login_mail}")
        username_field = self.wait.wait_for_element_to_be_clickable(self.login_email)
        username_field.clear()
        username_field.send_keys(login_mail)

    def enter_password(self, password):
        self.logger.info("Entering login password.")
        password_field = self.wait.wait_for_element_to_be_visible(self.login_pass)
        password_field.clear()
        password_field.send_keys(password)

    def register_username(self, username):
        self.logger.info(f"Registering username: {username}")
        name_field = self.wait.wait_for_element_to_be_visible(self.username_input)
        name_field.clear()
        name_field.send_keys(username)

    def register_email(self, email):
        self.logger.info(f"Registering email: {email}")
        email_field = self.wait.wait_for_element_to_be_visible(self.email_input)
        email_field.clear()
        email_field.send_keys(email)

    def submit_registration(self):
        self.logger.info("Submitting registration form.")
        self.wait.wait_for_element_to_be_visible(self.submit_reg).click()
        self.logger.info("Navigating to registration page.")

    def submit_login(self):
        self.logger.info("Submitting login form.")
        self.wait.wait_for_element_to_be_visible(self.login_btn).click()

    def verify_new_user_signup(self):
        self.logger.info("Verifying 'New User Signup!' page load.")
        return self.wait.wait_for_element_presence(self.verify_page).text == "New User Signup!"

    def verify_registration_submit_text(self):
        self.logger.info("Verifying 'Enter Account Information' on submit registration")
        return self.wait.wait_for_element_to_be_clickable(self.verify_submit_reg).text == "ENTER ACCOUNT INFORMATION"