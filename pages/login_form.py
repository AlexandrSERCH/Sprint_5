from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import Locators


class LoginForm:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_button_go_to_register(self):
        self.driver.find_element(*Locators.BUTTON_GO_TO_REGISTER).click()

    def enter_email(self, email):
        (WebDriverWait(self.driver, 3)
         .until(expected_conditions.element_to_be_clickable(Locators.FIELD_EMAIL)).send_keys(email))

    def enter_password(self, password):
        (WebDriverWait(self.driver, 3)
         .until(expected_conditions.element_to_be_clickable(Locators.FIELD_PASSWORD)).send_keys(password))

    def click_login_button(self):
        self.driver.find_element(*Locators.BUTTON_LOGIN_IN_AUTH_FORM).click()



