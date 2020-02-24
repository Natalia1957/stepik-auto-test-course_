# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_css_selector("button.btn").click()
browser.switch_to.alert.accept()
y = calc(int(browser.find_element_by_id("input_value").text))
browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_class_name("btn-primary").click()