# Импорт модулей и инициализация драйвера
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException
driver = webdriver.Chrome()
driver.wait = WebDriverWait(driver, 5)

# Ожидание элементов.
element = driver.wait.until(
    EC.presence_of_element_located(
        EC.element_to_be_clickable(
            EC.visibility_of_element_located(
                (By.NAME, "name")
                (By.ID, "id")
                (By.LINK_TEXT, "link text")
                (By.PARTIAL_LINK_TEXT, "partial link text")
                (By.TAG_NAME, "tag name")
                (By.CLASS_NAME, "class name")
                (By.CSS_SELECTOR, "css selector")
                (By.XPATH, "xpath")
            )
        )
    )
)
#Элемент button.click(), который и вызывал ошибку, находится внутри оператора try. Если ошибка возникла,
# мы взглянем на следующую кнопку, при помощи visibility_of_element_located, чтобы убедиться в том, что нужный
# нам элемент видим, после чего нажимаем на кнопку. Если в какой-либо момент, какой-либо элемент не будет найден
# в течение 5 секунд, ошибка TimeoutException возникнет и будет выявлена двумя последними строками кода.
# Обратите внимание на то, что название кнопки “btnK” , а название новой кнопки - “btnG”.