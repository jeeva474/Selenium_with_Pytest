""" For static dropdown - Use select class
    1. select_by_index(0) --- Index starts from 0
    2. select_by_visible_text("Male") ---
    3. select_by_value("name")--- use it only if you have value attribute in the select class

    Deselct --- Used only in Multi select(when one or more options selected you can use deselect
    to deselct one of the options
    1. deselect_by_index(0)
    2. deselect_by_visible_text("jeeva")
    3. deselect_by_value("") """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME, "name").send_keys("jeevanandham")
driver.find_element(By.CSS_SELECTOR, "input[name='email']").send_keys("jeeva474@gmail.com")
driver.find_element(By.ID, "exampleCheck1").click()
dropdowns = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))

dropdowns.select_by_index(0)
time.sleep(5)
dropdowns.select_by_visible_text("Female")
time.sleep(5)

driver.close()
