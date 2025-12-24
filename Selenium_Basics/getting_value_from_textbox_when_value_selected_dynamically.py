from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(5)
countries_list = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")
for country in countries_list:
    if country.text == "India":
        country.click()
country_selected = driver.find_element(By.ID, "autosuggest").get_attribute("value")
assert country_selected == "India", "Wrong country Name selected"
departure_city = Select(driver.find_element(By.ID, "ctl00_mainContent_ddl_originStation1"))
departure_city.select_by_value("AIP")
time.sleep(3)
