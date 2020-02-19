from selenium import webdriver
from math import log, sin
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

# Нажать на кнопку
browser.find_element_by_css_selector('button.btn.btn-primary').click()

# Принять confirm
browser.switch_to.alert.accept()

# на случай медленного интернета
time.sleep(1)

# решить капчу для роботов
browser.find_element_by_id('answer').send_keys(str(log(abs(12*sin(int(browser.find_element_by_id('input_value').text))))))
browser.find_element_by_css_selector('button.btn.btn-primary').click()