from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from Pytest_selenium import test_config

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

first_product_name = test_config.first_product
second_product_name = test_config.second_product

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

driver.find_element(By.LINK_TEXT, "Shop").click()

mobile_products = driver.find_elements(By.XPATH, "//app-card[@class='col-lg-3 col-md-6 mb-3']")

for mobile in mobile_products:
    mobile_name = mobile.find_element(By.XPATH, "div/div/h4/a").text
    if mobile_name == first_product_name or mobile_name == second_product_name:
        mobile.find_element(By.XPATH, "div/div[2]/button").click()
        time.sleep(5)

driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
driver.find_element(By.CSS_SELECTOR, ".btn.btn-success").click()
country_text_box = driver.find_element(By.ID, "country")
country_text_box.send_keys("Ind")

wait = WebDriverWait(driver, 10)
country = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
country.click()
country_selected = country_text_box.get_attribute('value')
assert country_selected == "India", "wrong country name selected or the field is empty"

driver.find_element(By.CSS_SELECTOR, ".checkbox-primary").click()

driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible").text
print(success_message)
assert "Thank you!" in success_message, "order not submitted properly"




