import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from config.config import Config


@pytest.fixture(scope="function")
def driver(request):
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")

    if Config.HEADLESS:
        options.add_argument("--headless=new")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(Config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.PAGE_LOAD_TIMEOUT)

    driver.get(Config.BASE_URL)
    driver.maximize_window()

    request.cls.driver = driver

    yield driver

    driver.quit()
