# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "Подтверждаю, что являюсь роботом".
# Переключить radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element_by_id("input_value").text)
y = calc(x)

browser.execute_script("window.scrollBy(0, 100);")

browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_class_name("btn-default").click()