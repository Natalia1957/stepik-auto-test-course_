import pytest
from selenium import webdriver
import time
import math

@pytest.mark.parametrize('linktext', ["https://stepik.org/lesson/236895/step/1","https://stepik.org/lesson/236896/step/1","https://stepik.org/lesson/236897/step/1","https://stepik.org/lesson/236898/step/1","https://stepik.org/lesson/236899/step/1","https://stepik.org/lesson/236903/step/1","https://stepik.org/lesson/236904/step/1","https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, linktext):
    browser.implicitly_wait(10)
    link = f"{linktext}"
    browser.get(link)
	
    text_el = browser.find_element_by_css_selector("textarea")
    answer = str(math.log(int(time.time())))
    text_el.send_keys(answer)
	
    button_el = browser.find_element_by_class_name("submit-submission")
    
    button_el.click()
	
    opt_hint = browser.find_element_by_class_name("smart-hints__hint")
    opt_hint_text = opt_hint.text
    assert opt_hint_text == "Correct!", opt_hint_text

