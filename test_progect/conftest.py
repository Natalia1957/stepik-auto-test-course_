import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="ru", help="Choose language")
    print("adoption")


@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language_ = request.config.getoption("language")
    print(f"language={language_}")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language_})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language_)
        browser = webdriver.Firefox()
    else:
        print("Browser {} still is not implemented".format(browser_name))
    yield browser
    browser.quit()

