from selenium.webdriver.chrome.webdriver import WebDriver

from locators.locators import Locators


class ProfilePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_title_created_card(self):
        title = (self.driver.find_element(*Locators.BLOCK_CREATED_PRODUCT_CARD)
                .find_element(*Locators.CREATED_PRODUCT_CARD_TITLE).text)

        return title

    def get_city_created_card(self):
        city = (self.driver.find_element(*Locators.BLOCK_CREATED_PRODUCT_CARD)
                .find_element(*Locators.CREATED_PRODUCT_CARD_CITY).text)

        return city

    def get_price_created_card(self):
        price = (self.driver.find_element(*Locators.BLOCK_CREATED_PRODUCT_CARD)
                .find_element(*Locators.CREATED_PRODUCT_CARD_PRICE).text)
        price = price.replace("₽", "").replace(" ", "")

        return int(price)

