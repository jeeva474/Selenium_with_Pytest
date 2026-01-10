import pytest
from Pytest_selenium.pageobjects.shoppage import Shoppage
import json

filepath = "../test_data/data.JSON"
with open(filepath) as json_file:
    test_data = json.load(json_file)
    mobile_list = test_data["product"]

@pytest.mark.usefixtures("setup")
@pytest.mark.parametrize("product_list", mobile_list)
@pytest.mark.smoketest
def test_shopproducts(setup, product_list):
    driver = setup
    driver.get("https://rahulshettyacademy.com/angularpractice/shop")
    shop_page = Shoppage(driver)
    print(shop_page.get_title())
    shop_page.add_to_cart(product_list["mobile_name"])
    checkout_page = shop_page.go_to_cart()
    delivery_page = checkout_page.checkout()
    delivery_page.country_selection(product_list["country"])
    delivery_page.purchase_order()
