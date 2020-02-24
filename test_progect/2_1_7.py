# Открыть страницу http://suninjuly.github.io/get_attribute.html.
# Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# Посчитать математическую функцию от x (сама функция остаётся неизменной).
# Ввести ответ в текстовое поле.
# Отметить checkbox "Подтверждаю, что являюсь роботом".
# Выбрать radiobutton "Роботы рулят!".
# Нажать на кнопку "Отправить".
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element_by_id("treasure").get_attribute("valuex"))
y = calc(x)
browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_class_name("btn-default").click()