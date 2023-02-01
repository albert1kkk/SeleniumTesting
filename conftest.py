import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("chrome") #Используй headless если не нужен UI
    options.add_argument("--start-maximized")
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    get_webdriver = webdriver.Chrome(executable_path="C:/Users/a2512/Desktop/Python Projects/Selenuim tests/chromedriver_win32/chromedriver.exe", options=options)
    yield get_webdriver

