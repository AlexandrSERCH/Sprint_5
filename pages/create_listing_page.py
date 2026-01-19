import random

from selenium.webdriver.ie.webdriver import WebDriver

from locators.locators import Locators


class CreateListingPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_name(self, name: str):
        self.driver.find_element(*Locators.FIELD_LISTING_NAME).send_keys(name)

    def enter_description(self, description: str):
        self.driver.find_element(*Locators.FIELD_LISTING_DESCRIPTION).send_keys(description)

    def enter_price(self, price: int):
        self.driver.find_element(*Locators.FIELD_LISTING_PRICE).send_keys(price)

    def select_random_category(self):
        self.driver.find_element(*Locators.DROPDOWN_LISTING_CATEGORY_BUTTON_OPEN_LIST).click()

        values = self.driver.find_elements(*Locators.DROPDOWN_LISTING_CATEGORY_LIST_VALUES)
        values[random.randint(0, 4)].click()

    def select_random_city(self):
        self.driver.find_element(*Locators.DROPDOWN_LISTING_CITY_BUTTON_OPEN_LIST).click()

        values = self.driver.find_elements(*Locators.DROPDOWN_LISTING_CITY_LIST_VALUES)
        values[random.randint(0, 5)].click()

    def select_pre_owned_radiobutton(self):
        self.driver.find_element(*Locators.RADIOBUTTON_LISTING_PRE_OWNED).click()

    def click_publish_button(self):
        self.driver.find_element(*Locators.BUTTON_LISTING_PUBLISH).click()