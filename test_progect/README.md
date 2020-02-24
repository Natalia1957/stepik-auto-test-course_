## Запуск автотестов для разных языков интерфейса
### Задание peer-to-peer курса Автоматизация тестирования с помощью Selenium и Python

### Пример вывода:
    (py36) C:\Users\Marat\PycharmProjects\stepik-selenium-3_6_9>pytest --language="es" -s test_items.py
    adoption
    ============================= test session starts =============================
    platform win32 -- Python 3.6.5, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
    rootdir: C:\Users\Marat\PycharmProjects\stepik-selenium-3_6_9, inifile:
    plugins: remotedata-0.2.1, openfiles-0.3.0, doctestplus-0.1.3, arraydiff-0.2
    collected 1 item
     
    test_items.py language=es
     
    DevTools listening on ws://127.0.0.1:51895/devtools/browser/d8b9c251-f42c-473c-b0b6-055076c5c807
    .
     
    ========================== 1 passed in 7.80 seconds ===========================
     
    (py36) C:\Users\Marat\PycharmProjects\stepik-selenium-3_6_9>