import conftest


class TestLoginUser:

    def test_login_user(self, driver, main_page, login_form, user_is_registered):
        main_page.click_login_button()
        login_form.enter_email(user_is_registered["login"])
        login_form.enter_password(user_is_registered["password"])
        login_form.click_login_button()

        assert main_page.avatar_is_displayed()
        assert conftest.base_url == driver.current_url
