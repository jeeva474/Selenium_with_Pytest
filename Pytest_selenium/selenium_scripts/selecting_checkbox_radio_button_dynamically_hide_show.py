""" if the checkbox and radio button ooptions keeps changing, It is better to use
the find_elemnets to store all the options and select the option by iterating through the elements"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)
print(driver.current_url)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
radio_buttons = driver.find_elements(By.XPATH, "//input[@class='radioButton']")
for checkbox in checkboxes:
    check_box_option = checkbox.get_attribute('value')
    if check_box_option == "option2":
        checkbox.click()
        assert checkbox.is_selected()
for radio in radio_buttons:
    if radio.get_attribute("value") == "radio1":
        radio.click()
        assert radio.is_selected()
display_box = driver.find_element(By.ID, "displayed-text")
assert display_box.is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
time.sleep(5)
assert not display_box.is_displayed()
driver.find_element(By.XPATH, "//input[@value='Show']").click()
assert display_box.is_displayed()
time.sleep(2)
driver.close()
