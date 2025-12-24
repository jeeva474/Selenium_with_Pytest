from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
driver.implicitly_wait(10)

""" when executing any action chain commands, perform() is mandatory"""

#move_to_element
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

#click_and_hold
# action.click_and_hold(driver.find_element(By.ID, "mousehover")).perform()

#double_click
# action.double_click(driver.find_element(By.ID, "mousehover")).perform()

#context click = right click
action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()

#move_to_element and click
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)
driver.close()