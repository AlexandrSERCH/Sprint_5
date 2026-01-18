from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import Locators


class CreateListingAlertForm:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_text_from_title(self):
        title_text = (WebDriverWait(self.driver, 3)
                      .until(expected_conditions.visibility_of_element_located(Locators.TITLE_FORM_CREATE_LISTING)).text)

        return title_text