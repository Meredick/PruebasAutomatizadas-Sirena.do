from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://sirena.do/"
    LOGIN_ICON = (By.CSS_SELECTOR, "i.fas.fa-caret-down")
    EMAIL_INPUT = (By.ID, "username_login-header")
    PASS_INPUT = (By.ID, "password_login-header")
    LOGIN_BUTTON = (By.ID, "submit_login-header")
    USER_BADGE = (By.ID, "container")  
    ERROR_MESSAGE = (By.ID, "swal2-html-container")
    
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self):
        self.driver.get(self.URL)

    def open_login_form(self):
        icon = self.wait.until(EC.element_to_be_clickable(self.LOGIN_ICON))
        icon.click()
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_INPUT))

    def login(self, email: str, password: str):
        self.open_login_form()
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)
        pass_input = self.driver.find_element(*self.PASS_INPUT)
        pass_input.clear()
        pass_input.send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def ensure_logged_in(self):
        self.wait.until(EC.visibility_of_element_located(self.USER_BADGE))
        
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE)).text   