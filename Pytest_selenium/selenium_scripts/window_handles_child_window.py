from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "openwindow").click()
windows = driver.window_handles
time.sleep(2)

driver.switch_to.window(windows[1])
time.sleep(2)
driver.find_element(By.LINK_TEXT, "Access all our Courses").click()
time.sleep(2)

driver.switch_to.window(windows[0])
time.sleep(2)

driver.find_element(By.ID, "opentab").click()
time.sleep(5)
opened_windows = driver.window_handles

driver.switch_to.window(opened_windows[1])
print(driver.title)

driver.close()
