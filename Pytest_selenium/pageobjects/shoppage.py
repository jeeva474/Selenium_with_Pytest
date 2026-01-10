from selenium.webdriver.common.by import By
from Pytest_selenium.pageobjects.checkoutpage import CheckoutPage
import time

from Pytest_selenium.utils.Browser_utils import BrowserUtils


class Shoppage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.shop = (By.LINK_TEXT, "Shop")
        self.mobile_products = (By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']")
        self.mobile_name = (By.XPATH, "div/div/h4/a")
        self.addcart_button = (By.XPATH, "div/div[2]/button")
        self.cart_select = (By.XPATH, "//a[contains(text(),'Checkout')]")

    def add_to_cart(self, first_product):
        self.driver.find_element(*self.shop).click()

        mobile_products = self.driver.find_elements(*self.mobile_products)

        for mobile in mobile_products:
            mobile_name = mobile.find_element(*self.mobile_name).text
            if mobile_name == first_product:
                mobile.find_element(*self.addcart_button).click()
                time.sleep(5)

    def go_to_cart(self):
        self.driver.find_element(*self.cart_select).click()
        checkout = CheckoutPage(self.driver)
        return checkout