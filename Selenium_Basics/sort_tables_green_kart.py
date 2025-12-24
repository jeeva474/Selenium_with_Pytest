from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

chrome_sorted_vegetables = []

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.LINK_TEXT, "Top Deals").click()

window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])

driver.find_element(By.XPATH, "//th[@aria-label='Veg/fruit name: activate to sort column ascending']").click()
time.sleep(3)
vegetables = driver.find_elements(By.XPATH, "//tr/td[1]")
for vegetable in vegetables:
    chrome_sorted_vegetables.append(vegetable.text)

sorted_list = sorted(chrome_sorted_vegetables)
assert chrome_sorted_vegetables == sorted_list, "Broswer sorted list seems to be wrong"



