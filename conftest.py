import random
import string

import pytest
from selenium import webdriver
import requests
from  data import CommonData
from links import Links

@pytest.fixture(scope='function')
def driver():
    # Открываем браузер
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    # Закрываем браузер после завершения всех тестов
    driver.quit()


@pytest.fixture(scope='session')
def create_user():
    """Создаёт пользователя перед тестом и удаляет после теста."""
    username = CommonData.random_name
    email = CommonData.random_email
    password = CommonData.password
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', json={
        "email": email,
        "password": password,
        "name": username
    })

    assert response.status_code == 200
    user_data = response.json()

    yield user_data, password
    requests.delete("https://stellarburgers.nomoreparties.site/api/auth/user", headers={
        "Authorization": f"Bearer {user_data['accessToken']}"
    })