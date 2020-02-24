from selenium import webdriver
import time

def link_t(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_xpath(".//*[@placeholder = 'Введите имя']").send_keys("Иван")
    browser.find_element_by_xpath(".//*[@placeholder = 'Введите фамилию']").send_keys("Иванов")
    browser.find_element_by_xpath(".//*[@placeholder = 'Введите Email']").send_keys("ivan@yandex.ru")
    browser.find_element_by_css_selector("button.btn").click()

    time.sleep(1)
    return browser.find_element_by_tag_name("h1").text

def test_reg1():
    assert link_t("http://suninjuly.github.io/registration1.html") == "Поздравляем! Вы успешно зарегистировались!", \
        "registration is failed"


def test_reg2():
    assert link_t("http://suninjuly.github.io/registration2.html") == "Поздравляем! Вы успешно зарегистировались!", \
        "registration is failed"
