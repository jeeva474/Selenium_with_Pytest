from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from Pytest_selenium.utils.Browser_utils import BrowserUtils


class DeliveryPage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.country = (By.ID, "country")
        self.agree_terms = (By.CSS_SELECTOR, ".checkbox-primary")
        self.purchase = (By.XPATH, "//input[@value='Purchase']")
        self.alert = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def country_selection(self, country_to_be_searched):
        country_text_box = self.driver.find_element(*self.country)
        country_text_box.send_keys(country_to_be_searched)

        wait = WebDriverWait(self.driver, 10)
        country = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "India")))
        country.click()
        country_selected = country_text_box.get_attribute('value')
        assert country_selected == "India", "wrong country name selected or the field is empty"

    def purchase_order(self):
        self.driver.find_element(*self.agree_terms).click()
        self.driver.find_element(*self.purchase).click()
        success_message = self.driver.find_element(*self.alert).text
        print(success_message)
        assert "Thank you!" in success_message, "order not submitted properly"