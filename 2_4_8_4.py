from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import pyperclip

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

# Дождаться, когда цена дома уменьшится до $100
WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

# Нажать на кнопку "Забронировать"
browser.find_element_by_id('book').click()

# Решить уже известную нам математическую задачу (используйте ранее написанный код)
browser.find_element_by_id('answer').send_keys(
  str(log(abs(12*sin(int(browser.find_element_by_id('input_value').text)))))
)
browser.find_element_by_id('solve').click()

# Копирование числа из алерта в буфер обмена
alert = browser.switch_to.alert
alert_text = alert.text
addToClipBoard = alert_text.split(': ')[-1]
pyperclip.copy(addToClipBoard)
