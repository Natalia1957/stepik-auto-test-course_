import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestAbs(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(5)


    def test_test1(self):
        browser, success = self.unit_browser1()
        self.open_home_page(browser, " http://suninjuly.github.io/registration2.html")
        self.type1(browser, "div.first_block input.first", "Natalia")
        self.type1(browser, "div.first_block input.second", "Nilsen")
        self.type1(browser, "div.first_block input.third", "mikhnat@mail.ru")
        self.click1(browser, "button")
        self.welcome_text(browser, "h1")

    def welcome_text(self, browser, locator ):
        welcome_text = browser.find_element(By.TAG_NAME, locator).text
        self.assertEqual("Registration", welcome_text)
        return

    def click1(self, browser, locator):
        self.click = browser.find_element_by_css_selector(locator).click

    def type1(self, browser, locator, text):
        browser.find_element_by_css_selector(locator).click
        browser.find_element_by_css_selector(locator).clear
        browser.find_element_by_css_selector(locator).send_keys(text)
        self.assertTrue(browser.find_element_by_css_selector(locator))

    def unit_browser1(self):
        success = True
        browser = self.browser
        return browser, success

    def open_home_page(self, browser, url1):
        browser.get(url1)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__":
    unittest.main()


