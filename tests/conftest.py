import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


@pytest.fixture()
def launcher_web():
    service = Service()
    option = webdriver.ChromeOptions()
    option.add_argument("--lang=zh-TW")
    option.add_argument("--incognito")
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=option)
    driver.get("https://stage.myviewboard.com/signin")
    return driver
