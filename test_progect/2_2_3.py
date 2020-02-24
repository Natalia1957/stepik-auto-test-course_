# Открыть страницу http://suninjuly.github.io/selects1.html
# Посчитать сумму заданных чисел
# Выбрать в выпадающем списке значение равное расчитанной сумме
# Нажать кнопку "Отправить"

from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element_by_id("num1").text) + int(browser.find_element_by_id("num2").text)
Select(browser.find_element_by_id("dropdown")).select_by_value(str(x))
browser.find_element_by_class_name("btn-default").click()