from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)

driver.switch_to.frame("courses-iframe")
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Learning Paths").click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.find_element(By.NAME, "enter-name").send_keys("Jeeva")
time.sleep(3)
driver.close()