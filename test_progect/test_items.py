from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestItems:
    def test_check_add_to_cart(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(2)
        assert len(browser.find_elements( By.CLASS_NAME, "btn-add-to-basket")) == 1
