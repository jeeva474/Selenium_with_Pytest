from Pytest_selenium.pageobjects.loginpage import Loginpage
import pytest
import json
file_path = "../test_data/data.JSON"

with open(file_path) as f:
    data = json.load(f)
    test_list = data["data"]

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("test_list_item", test_list)
def test_signup_check(setup, test_list_item):
    driver = setup
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    loginpage = Loginpage(driver)
    loginpage.login(test_list_item["username"],  test_list_item["password"])
