""" for Handling Javscript popups, use switch_to.alert
    accept() - to accept the alert(i.e click OK)
    dismiss() - to select cancel in the alert popup"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

driver.find_element(By.NAME, "enter-name").send_keys("Jeeva")

#selecting alert button
driver.find_element(By.ID, "alertbtn").click()

#Switching to alert to get the alert text
alert = driver.switch_to.alert
print(alert.text)
#accept the alert
alert.accept()

#after accepting the alert, switch back to same HTML content using default_content
driver.switch_to.default_content()


driver.find_element(By.ID, "confirmbtn").click()
confirm_alert = driver.switch_to.alert
# dismiss() is to cancel the alert
confirm_alert.dismiss()

driver.close()
