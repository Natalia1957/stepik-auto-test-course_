# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Отправить"
from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

browser.find_element_by_xpath(".//*[@placeholder = 'Введите имя']").send_keys("Иван")
browser.find_element_by_xpath(".//*[@placeholder = 'Введите фамилию']").send_keys("Иванов")
browser.find_element_by_xpath(".//*[@placeholder = 'Введите Email']").send_keys("ivan@yandex.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'test.txt')
browser.find_element_by_id("file").send_keys(file_path)
time.sleep(1)

button = browser.find_element_by_css_selector("button.btn")
button.click()