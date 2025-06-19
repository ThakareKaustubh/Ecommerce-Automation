import allure
from pages.login_page import LoginPage
from pages.products import ProductPage
from utils.create_user_api import create_user_from_api
from utils.delete_user_api import delete_user_from_api
import pytest


@allure.feature("Veirfy Product Page")
@allure.story("Products Page")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
# @pytest.mark.flaky(reruns=2, reruns_delay=4)
def test_verify_products_page(driver_setup, base_url):
    valid_email, valid_password, valid_username = create_user_from_api(base_url)
    driver = driver_setup
    driver.get(base_url)

    with allure.step("Verify Home page loaded"):
        loginpage = LoginPage(driver)
        assert loginpage.check_page_load(), "Home Page did not load"

    with allure.step("Navigate to login/signup page"):
        loginpage.goto_login_signup_page()
        assert (
            loginpage.verify_login_to_acc_is_visible()
        ), "Login to your account not visible"

    with allure.step("Entering valid credentials"):
        loginpage.enter_username(valid_email)
        loginpage.enter_password(valid_password)
        loginpage.submit_login()

    with allure.step("Click on products page"):
        product_Page = ProductPage(driver)
        product_Page.goto_products_page()

    with allure.step("Verify navigation to products page"):
        assert product_Page.verify_navigation_to_products(), "Product page navigation has failed"

    with allure.step("Verify Products list is visible"):
        assert product_Page.check_products_list_visible(), "Products list is not visible on the Products page"

    with allure.step("Click on first product in the list"):
        product_Page.click_on_first_product()

    with allure.step("Verify user landed on user details page"):
        assert product_Page.verify_product_details_page(), "1 or more product details are not visible"
        delete_user_from_api(base_url,valid_email,valid_password)