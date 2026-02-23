import pytest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class HomePage(BasePage):

    # Locators
    COOKIE = (By.ID, "wt-cli-accept-all-btn")
    WE_ARE_HIRING_LINK = (By.CSS_SELECTOR, "a[data-text=\"We're hiring\"]")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL

    def accept_cookies(self):
        try:
            cookie_btn = self.wait_for_element_clickable(self.COOKIE,timeout=Config.IMPLICIT_WAIT)
            cookie_btn.click()
        except Exception as e:
            pytest.fail(f"Cookie could not be accepted! {e}")



    def homepage_verify(self):
        current_url = self.get_current_url()
        if Config.BASE_URL == current_url:
            print ("Homepage Verified")
        else:
            raise Exception(f"HomePage açılamadı. Current URL: {current_url}")

    def go_to_career_page(self):
        self.driver.save_screenshot("before_click.png")
        print("Current URL:", self.driver.current_url)
        print("Page title:", self.driver.title)
        self.driver.get("https://insiderone.com/careers/")