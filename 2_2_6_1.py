from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input_y = browser.find_element_by_id("answer").send_keys(y)
    browser.execute_script("window.scrollBy(0,150);")
    option1 = browser.find_element_by_css_selector("#robotCheckbox").click()
    option2 = browser.find_element_by_css_selector("#robotsRule").click()
    button = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()
