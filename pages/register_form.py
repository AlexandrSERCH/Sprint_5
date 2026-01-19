import time

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.locators import Locators


class ResisterForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_email(self, email: str):
        (WebDriverWait(self.driver, 5)
         .until(expected_conditions.element_to_be_clickable(Locators.FIELD_EMAIL)).send_keys(email))

    def get_text_error_field_email(self):
        text = (WebDriverWait(self.driver, 5)
                .until(expected_conditions.visibility_of_element_located(Locators.FIELD_REGISTER_EMAIL_ERROR)).text)
        return text

    def enter_password(self, password: str):
        self.driver.find_element(*Locators.FIELD_PASSWORD).send_keys(password)

    def enter_password_submit(self, password: str):
        self.driver.find_element(*Locators.FIELD_SUBMIT_PASSWORD).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*Locators.BUTTON_REGISTER).click()

    def fields_with_errors_is_red(self):
        fields = self.driver.find_elements(*Locators.FIELDS_WITH_ERROR)

        result = []

        for field in fields:
            color_from_browser = field.value_of_css_property("border-color")
            r, g, b = color_from_browser[color_from_browser.find("(")+1:color_from_browser.find(")"):].split(",")
            result.append(int(r) > 200 and int(g) < 150 and int(b) < 150)

        return all(result)