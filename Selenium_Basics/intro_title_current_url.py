from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.chrome.service import Service

# service_obj = Service("C:/Users/jrameshb/Downloads/chromedriver-win64/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver = webdriver.Edge() # for running the tests in Edge Browser
driver = webdriver.Firefox() # for running the tests in Firefox Browser
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
print(driver.title)
print(driver.current_url)
assert driver.current_url == "https://www.facebook.com/", "current_URL not matching with the URL provided"
driver.find_element(By.ID, "email").send_keys("jeevanandham5696@gmail.com")
driver.find_element(By.ID, "pass").send_keys("jeevajeev")
driver.find_element(By.NAME, "login").click()
time.sleep(3)
driver.close()

