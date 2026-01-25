import conftest
from conftest import driver, main_page
from faker import Faker


class TestRegisterUser:

    def test_register_user(self, driver, main_page, login_form, register_form):
        faker = Faker()
        login = faker.email()
        password = faker.password()

        main_page.click_login_button()
        login_form.click_button_go_to_register()
        register_form.register_user(login, password)

        actual_username_in_header = main_page.get_username_from_header()

        assert actual_username_in_header == "User."
        assert main_page.avatar_is_displayed()
        assert conftest.base_url == driver.current_url

    def test_validation_error_when_email_is_invalid(self, main_page, login_form, register_form):
        faker = Faker()
        login = faker.email().replace("@", "",).replace(".", "")

        main_page.click_login_button()
        login_form.click_button_go_to_register()
        register_form.enter_email(login)
        register_form.click_register_button()

        assert register_form.fields_with_errors_is_red()

        actual_error_text = register_form.get_text_error_field_email()
        assert actual_error_text == "Ошибка"

    def test_register_existing_user(self, main_page, login_form, register_form, user_is_registered):
        main_page.click_login_button()
        login_form.click_button_go_to_register()
        register_form.enter_email(user_is_registered["login"])
        register_form.enter_password(user_is_registered["password"])
        register_form.enter_password_submit(user_is_registered["password"])
        register_form.click_register_button()

        assert register_form.fields_with_errors_is_red()

        actual_error_text = register_form.get_text_error_field_email()
        assert actual_error_text == "Ошибка"

