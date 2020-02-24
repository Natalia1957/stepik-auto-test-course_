from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
#pytest --language=es test_items.py

@pytest.mark.usefixtures("browser")
class TestItems:
    def test_check_btn_add_to_basket(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        assert len(browser.find_elements( By.CLASS_NAME, "btn-add-to-basket")) == 1
