"""Locators Type
ID
NAME
CLASS_NAME --- By.
CSS_SELECTOR --- tagname[@attribute='value] -- input[id='name']
                for ID --- you can use #value of ID -- #inputvalue1
                for Class Name -- you can use - .value of class name --- .alert-success
XPATH ---- //tagname[@attribute='value'] -- //input[@id='name']
LINK_TEXT
PARTIAL_LINK_TEXT
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service("C:/Users/jrameshb/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.title)
print(driver.current_url)
time.sleep(3)
driver.find_element(By.NAME, "name").send_keys("jeeva474")  # NAME
driver.find_element(By.NAME, "email").send_keys("jeeva474747@gmail.com")
# driver.find_element(By.ID, "exampleInputPassword1").send_keys("Thanos@2026") # ID
driver.find_element(By.CSS_SELECTOR, "#exampleInputPassword1").send_keys("Thanos@2026")  # CSS_SELECTOR with ID
driver.find_element(By.XPATH, "//input[@type='checkbox']").click()  # XPATH
driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
time.sleep(3)
# message = driver.find_element(By.CLASS_NAME, "alert-success").text # CLASS NAME
message = driver.find_element(By.CSS_SELECTOR, ".alert-success").text  # CSS_SELECTOR with class name
print(message)
assert "Success!" in message, "The Form is not submitted properly"
driver.close()
