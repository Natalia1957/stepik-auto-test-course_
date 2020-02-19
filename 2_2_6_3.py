from selenium import webdriver
import time
from math import sin
from math import log

link ="http://SunInJuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)

    def lookup1(locator):

        x_element = browser.find_element_by_css_selector(locator)
        x = int(x_element.text)
        return x

    def calc(x):
        y = log(abs(12 * sin(x)))
        return y

    def type1_capture(locator, v):
        browser.execute_script("window.scrollBy(0, 120);")
        element1 = browser.find_element_by_css_selector(locator).send_keys(v)

    def click1(locator):
        b = browser.find_element_by_css_selector(locator)
        browser.execute_script("return arguments[0].scrollIntoView(true);", b)
        b.click()

    x2 = int(lookup1('#input_value'))
    y2 = str(calc(x2))
    type1_capture('#answer', y2)
    click1('#robotCheckbox')
    click1('#robotsRule')
    click1("button[type='submit']")

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(15)
    browser.quit()
