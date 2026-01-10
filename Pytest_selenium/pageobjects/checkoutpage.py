from Pytest_selenium.pageobjects.deliverypage import DeliveryPage
from selenium.webdriver.common.by import By
from Pytest_selenium.utils.Browser_utils import BrowserUtils


class CheckoutPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.checkout_select = (By.CSS_SELECTOR, ".btn.btn-success")

    def checkout(self):
        self.driver.find_element(*self.checkout_select).click()
        delivery_page = DeliveryPage(self.driver)
        return delivery_page