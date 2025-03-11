import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    # Открываем браузер
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # Закрываем браузер после завершения всех тестов
    driver.quit()