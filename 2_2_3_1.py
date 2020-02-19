from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

num1_element = browser.find_element_by_id('num1')
num1 = num1_element.text
print(num1)
num2_element = browser.find_element_by_id('num2')
num2 = num2_element.text
print(num2)
result = int(num1) + int(num2)
print(result)

select = Select(browser.find_element_by_id('dropdown'))
select.select_by_visible_text(str(result))

option = browser.find_element_by_css_selector("[type='submit']")
option.click()