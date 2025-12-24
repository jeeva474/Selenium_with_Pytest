""" For dynamic dropdown (Auto-suggestive dropdown)

    You have to use find_elements to store the all the elements in dropdown
    Iterate through the list and select the element that you want to click

    find_elements --- stores the elements in the list
    if no elements captured it will return a empty list"
    """
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
# from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
time.sleep(5)
driver.find_element(By.ID, "autosuggest").send_keys("Ind")
time.sleep(3)

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']/a")

for country in countries:
    if country.text == "India":
        country.click()
        break
try:
    wait = WebDriverWait(driver, 10)
    from_dropdown = wait.until(EC.element_to_be_clickable(
        (By.ID, "ctl00_mainContent_ddl_originStation1_CT")  # Visible clickable box
    ))
    from_dropdown.click()

    # 2. Click "Chennai (MAA)" from the list
    chennai_option = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='Chennai (MAA)']")
    ))
    chennai_option.click()
    arrival_city = Select(driver.find_element(By.ID, "ctl00_mainContent_ddl_destinationStation1"))
    arrival_city.select_by_value("DEL")
    driver.find_element(By.XPATH, "//input[@id='ctl00_mainContent_view_date1']").send_keys("02/02")
    currency = Select(driver.find_element(By.ID, "ctl00$mainContent$DropDownListCurrency"))
    currency.select_by_index(1)
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.close()
