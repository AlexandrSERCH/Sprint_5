import pytest
from faker import Faker
from selenium import webdriver

from pages.create_listing_page import CreateListingPage
from pages.create_listing_alert_form import CreateListingAlertForm
from pages.login_form import LoginForm
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.register_form import ResisterForm

base_url = "https://qa-desk.stand.praktikum-services.ru/"

@pytest.fixture(scope="function", autouse=True)
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def login_form(driver):
    return LoginForm(driver)

@pytest.fixture
def register_form(driver):
    return ResisterForm(driver)

@pytest.fixture
def create_listing_alert_form(driver):
    return CreateListingAlertForm(driver)

@pytest.fixture
def create_listing_page(driver):
    return CreateListingPage(driver)

@pytest.fixture
def profile_page(driver):
    return ProfilePage(driver)

@pytest.fixture
def user_is_registered(driver, main_page, login_form, register_form):
    faker = Faker()
    login = faker.email()
    password = faker.password()

    main_page.click_login_button()
    login_form.click_button_go_to_register()
    register_form.enter_email(login)
    register_form.enter_password(password)
    register_form.enter_password_submit(password)
    register_form.click_register_button()
    main_page.click_logout_button()

    return {"login": login, "password": password}

@pytest.fixture
def user_is_auth(driver, main_page, login_form, user_is_registered):
    main_page.click_login_button()
    login_form.enter_email(user_is_registered["login"])
    login_form.enter_password(user_is_registered["password"])
    login_form.click_login_button()
