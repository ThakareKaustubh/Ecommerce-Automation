from pages.base_page import BasePage
from utils.wait_utils import WaitUtils
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WaitUtils(driver, timeout=10)
        self.verify_product_page = (By.XPATH, "//h2[text()='All Products']")
        self.products_list = (By.CLASS_NAME, "features_items")
        self.first_product_view = (By.XPATH, "//li/a[@href='/product_details/1']")
        self.product_availability = (By.XPATH, "//p/b[text()='Availability:']")
        self.product_name = (By.XPATH, "//div[@class='product-information']/h2")
        self.product_category = (By.XPATH, "//div[@class='product-information']/p[1]")
        self.product_price = (By.XPATH, "//div[@class='product-information']/span/span")
        self.product_condition = (By.XPATH, "//div[@class='product-information']/p[3]/b")
        self.product_brand = (By.XPATH, "//div[@class='product-information']/p[4]/b")

    def verify_navigation_to_products(self):
        try:
            self.logger.info("Checking if navigated to Products page")
            verify_products = self.wait.wait_for_element_to_be_visible(self.verify_product_page)
            curr_url = self.driver.current_url
            if "products" in curr_url:
                if verify_products:
                    self.logger.info("Navigated successfully to products page")
                    return True
        except Exception as e:
            self.logger.error(e)

    def check_products_list_visible(self):
        self.logger.info("Checking if products list is visible")
        try:
            product_list = self.wait.wait_for_element_to_be_visible(self.products_list)
            if product_list:
                self.logger.info("List is visible")
                return True
        except Exception as e:
            self.logger.error(e)

    def click_on_first_product(self):
        self.logger.info("Clicking on first product card")
        try:
            first_product = self.wait.wait_for_element_to_be_clickable(self.first_product_view)
            first_product.click()
            self.wait.wait_for_element_to_be_visible(self.product_name)
        except Exception as e:
            self.logger.error(e)

    def verify_product_details_page(self):
        self.logger.info("Checking products details")
        try:
            self.logger.info("Will attempt to get driver current url")
            curr_url = self.driver.current_url
            self.logger.info(f"{curr_url}")
            if curr_url.endswith("product_details/1"):
                self.logger.info("sdvdfvsrfv")
                if (
                        self.wait.wait_for_element_to_be_visible(self.product_name)
                        and self.wait.wait_for_element_to_be_visible(self.product_category)
                        and self.wait.wait_for_element_to_be_visible(self.product_price)
                        and self.wait.wait_for_element_to_be_visible(self.product_availability)
                        and self.wait.wait_for_element_to_be_visible(self.product_condition)
                        and self.wait.wait_for_element_to_be_visible(self.product_brand)
                ):
                    self.logger.info("All product details visible")
                    return True
        except Exception as e:
                self.logger.warning("One or more product details not visible")
                return False



