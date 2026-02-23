import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
from config.config import Config


@pytest.fixture(scope="function")
def driver(request):
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.set_window_size(1920, 1080)  # bunu ekle
    driver.implicitly_wait(Config.IMPLICIT_WAIT)

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

    driver.get(Config.BASE_URL)
    driver.maximize_window()

    request.cls.driver = driver

    yield driver

    driver.quit()
