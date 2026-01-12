from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from Pytest_selenium.utils.Browser_utils import BrowserUtils


class Loginpage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.ID, "username")
        self.password = (By.XPATH, "//input[@type='password']")
        self.click_checkbox = (By.ID, "terms")
        self.signin_button = (By.ID, "signInBtn")
        self.dropdown = (By.CSS_SELECTOR, "select.form-control")
        self.signin_message = (By.CSS_SELECTOR, "div.alert-danger")

    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.click_checkbox).click()
        profession = Select(self.driver.find_element(*self.dropdown))
        profession.select_by_value("teach")
        self.driver.find_element(*self.signin_button).click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(ec.visibility_of_element_located(self.signin_message))
        signin_message = self.driver.find_element(*self.signin_message).text
        print(signin_message)
        assert "Incorrrrrect" in signin_message


