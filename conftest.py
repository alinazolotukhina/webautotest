import pytest
import yaml
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Функция для получения токена аутентификации
@pytest.fixture(scope='session')
def auth_token(request):
    config = yaml.safe_load(open("testdata.yaml"))
    login_url = f"{config['site_url']}/gateway/login"
    credentials = {
        "username": config["username"],
        "password": config["password"]
    }

    response = requests.post(login_url, json=credentials)
    assert response.status_code == 200, f"Failed to authenticate. Status code: {response.status_code}"

    token = response.json()["token"]
    return token

# Используем фикстуру для инициализации браузера
@pytest.fixture(scope='session')
def browser():
    # Инициализация браузера в зависимости от настроек в файле testdata.yaml
    with open('testdata.yaml') as f:
        testdata = yaml.safe_load(f)

    if testdata['browser'] == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata['browser'] == 'chrome':
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

    driver.maximize_window()
    yield driver
    driver.quit()
