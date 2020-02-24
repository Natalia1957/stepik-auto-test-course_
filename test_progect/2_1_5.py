from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


# программа должна выполнить следующие шаги:
#
# Открыть страницу http://suninjuly.github.io/math.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x (код для этого приведён ниже).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку Отправить.

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

x = int(browser.find_element_by_id("input_value").text)
y = calc(x)
browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_class_name("btn-default").click()




