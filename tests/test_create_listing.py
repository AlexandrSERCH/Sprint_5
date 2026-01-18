import random

from faker import Faker
import faker_commerce


class TestCreateListing:

    def test_create_listing_by_unauthorized_user(self, main_page, create_listing_alert_form):
        main_page.click_create_listing()
        actual_text_in_title_create_listing_form = create_listing_alert_form.get_text_from_title()

        assert actual_text_in_title_create_listing_form == "Чтобы разместить объявление, авторизуйтесь"

    def test_create_listing_by_authorized_user(self, main_page, user_is_auth, create_listing_page, profile_page):
        faker = Faker()
        faker.add_provider(faker_commerce.Provider)

        name = faker.ecommerce_name()
        description = faker.text()
        price = random.randint(1, 999999)

        main_page.click_create_listing()
        create_listing_page.enter_name(name)
        create_listing_page.enter_description(description)
        create_listing_page.enter_price(price)
        create_listing_page.select_random_category()
        create_listing_page.select_random_city()
        create_listing_page.select_pre_owned_radiobutton()
        create_listing_page.click_publish_button()
        main_page.click_on_avatar()

        actual_title = profile_page.get_title_created_card()
        actual_city = profile_page.get_city_created_card()
        actual_price = profile_page.get_price_created_card()

        assert actual_title == name
        assert actual_city == actual_city
        assert actual_price == price
