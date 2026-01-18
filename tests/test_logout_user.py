

class TestLogoutUser:


    def test_logout_user(self, main_page, login_form, user_is_registered):
        main_page.click_login_button()
        login_form.enter_email(user_is_registered["login"])
        login_form.enter_password(user_is_registered["password"])
        login_form.click_login_button()
        main_page.click_logout_button()

        assert main_page.login_button_is_displayed()
        assert not main_page.avatar_is_displayed()
        assert not main_page.username_is_displayed()

