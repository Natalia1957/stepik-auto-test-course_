# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Забронировать"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )
browser.find_element_by_class_name("btn-primary").click()

y = calc(int(browser.find_element_by_id("input_value").text))
browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_id("solve").click()

