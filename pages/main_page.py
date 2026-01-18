from selenium.common import StaleElementReferenceException
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.locators import Locators


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def login_button_is_displayed(self):
        login_button = (WebDriverWait(self.driver, 3)
         .until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_IN_HEADER)))

        return login_button.is_displayed()

    def click_login_button(self):
        (WebDriverWait(self.driver, 3)
         .until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGIN_IN_HEADER)).click())

    def username_is_displayed(self):
        try:
            username = (WebDriverWait(self.driver, 3)
                        .until(expected_conditions.visibility_of_element_located(Locators.USERNAME_IN_HEADER)))
            return username.is_displayed()
        except:
            return False

    def get_username_from_header(self):
        username = (WebDriverWait(self.driver, 3)
                    .until(expected_conditions.visibility_of_element_located(Locators.USERNAME_IN_HEADER)).text)

        return username

    def avatar_is_displayed(self):
        try:
            avatar = (WebDriverWait(self.driver, 3)
                      .until(expected_conditions.visibility_of_element_located(Locators.AVATAR_IN_HEADER)))
            return avatar.is_displayed()
        except:
            return False

    def click_on_avatar(self, retries=5):
        for attempt in range(retries):
            try:
                (WebDriverWait(self.driver, 5)
                 .until(expected_conditions.element_to_be_clickable(Locators.AVATAR_IN_HEADER_SVG))).click()
            except StaleElementReferenceException:
                if attempt == retries -1:
                    raise "Не удалось кликнуть по кнопке аватара. DOM не успел прогрузиться"

    def click_logout_button(self):
        (WebDriverWait(self.driver, 3)
         .until(expected_conditions.visibility_of_element_located(Locators.BUTTON_LOGOUT)).click())

    def click_create_listing(self, retries=5):
        for attempt in range(retries):
            try:
                return (WebDriverWait(self.driver, 5)
                 .until(expected_conditions.element_to_be_clickable(Locators.BUTTON_CREATE_LISTING)).click())
            except StaleElementReferenceException:
                if attempt == retries -1:
                    raise "Не удалось кликнуть по кнопке создания объявления. DOM не успел прогрузиться"
