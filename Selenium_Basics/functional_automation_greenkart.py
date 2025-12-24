from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(2)
products = driver.find_elements(By.XPATH, "//div[@class='product']")

expected_list = ["Cucumber - 1 Kg", "Raspberry - 1/4 Kg", "Strawberry - 1/4 Kg"]
actual_product_list = []

for product in products:
    product_name = product.find_element(By.XPATH, "h4").text
    actual_product_list.append(product_name)
    product_price = product.find_element(By.XPATH, "p[@class='product-price']").text
    product.find_element(By.XPATH, "div[3]/button").click()

assert expected_list == actual_product_list

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button[text()='PROCEED TO CHECKOUT']").click()
# if checkout_button.text == "PROCEED TO CHECKOUT":
#     checkout_button.click()

driver.find_element(By.CLASS_NAME, "promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
promo_code_applied = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo"))).text
print(promo_code_applied)
assert promo_code_applied == "Code applied ..!"

# validate the total amount with the total of each products
product_total = 0
products_prices = driver.find_elements(By.XPATH, "//tr/td[5]/p[@class='amount']")
for prices in products_prices:
    product_total += int(prices.text)
print(product_total)
total_amount = int(driver.find_element(By.CLASS_NAME, "totAmt").text)


assert total_amount == product_total, "total amount displayed in the page is wrong"

print(f"total amount: {total_amount}")
discount_amount = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
print(f"discount amount: {discount_amount}")

assert discount_amount < float(total_amount), "discount not applied"
driver.close()
