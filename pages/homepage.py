from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config.config import Config


class HomePage(BasePage):

    # Locators
    COOKIE = (By.ID, "wt-cli-accept-all-btn")
    WE_ARE_HIRING_LINK = (By.CSS_SELECTOR, "#footer > div.footer-wrapper > div > div > div.row > div:nth-child(3) > div > div:nth-child(5) > div > div.footer-links-col-item-body > a:nth-child(6)")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.BASE_URL

    def accept_cookies(self):
        try:
            cookie_btn = self.wait_for_element_clickable(self.COOKIE,timeout=Config.IMPLICIT_WAIT)
            cookie_btn.click()
        except Exception:
            pass

    def homepage_verify(self):
        current_url = self.get_current_url()
        if Config.BASE_URL == current_url:
            print ("Homepage Verified")
        else:
            raise Exception(f"HomePage açılamadı. Current URL: {current_url}")

    def go_to_career_page(self):
        self.safe_click(self.WE_ARE_HIRING_LINK)
