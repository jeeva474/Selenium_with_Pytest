from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.implicitly_wait(10)
radio_buttons = driver.find_elements(By.NAME, "radioButton")
check_boxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for button in radio_buttons:
    if button.get_attribute('value') == 'radio2':
        button.click()
        assert button.is_selected()
time.sleep(5)
for checkbox in check_boxes:
    if checkbox.get_attribute('value') == 'option3':
        checkbox.click()
        assert checkbox.is_selected()
time.sleep(5)
displayed_text_box = driver.find_element(By.ID, "displayed-text")
assert displayed_text_box.is_displayed()
displayed_text_box.send_keys("something")
time.sleep(5)

driver.find_element(By.ID, "hide-textbox").click()
assert not displayed_text_box.is_displayed()
time.sleep(5)


driver.find_element(By.ID, "show-textbox").click()
assert displayed_text_box.is_displayed()
time.sleep(3)

driver.find_element(By.XPATH, "//input[@id='name']").send_keys("jeeva")
driver.find_element(By.ID, "alertbtn").click()

alerts = driver.switch_to.alert
alerts.accept()
driver.switch_to.default_content()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input[id='confirmbtn']").click()
confirm_alert = driver.switch_to.alert
confirm_alert.dismiss()




