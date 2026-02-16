from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, ElementClickInterceptedException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from config.config import Config


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def get_elements(self, locator):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located(locator))

    def wait_element_visibility(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        return element

    def wait_element_presence(self, locator):
        element = WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(locator))
        return element

    def wait_elements_presence(self, locator):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_by_index_safe(self, locator, index: int):
        wait = WebDriverWait(self.driver, 30)

        wait.until(EC.presence_of_all_elements_located(locator))
        elements = self.driver.find_elements(*locator)

        if index >= len(elements):
            raise IndexError(
                f"Requested index {index} but only {len(elements)} elements found"
            )

        element = elements[index]
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});", element
        )
        self.driver.execute_script("window.scrollBy(0, -120);")

        wait.until(EC.visibility_of(element))

        try:
            element.click()
        except Exception:
            self.driver.execute_script("arguments[0].click();", element)


    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url):
        self.driver.get(url)

    def wait_for_element_clickable(self, locator, timeout=None):
        wait_time = timeout if timeout else Config.EXPLICIT_WAIT
        return WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        )

    def accept_cookies(self):
        try:
            cookie_btn = self.wait_for_element_clickable(Config.COOKIES,timeout=Config.IMPLICIT_WAIT)
            cookie_btn.click()
        except TimeoutException:
            pass

    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.driver.execute_script("window.scrollBy(0, -100);")
        return element

    def verify_url(self, expected_part):
        current_url = self.driver.current_url
        if expected_part not in current_url:
            raise Exception(
                f"URL doğrulanamadı. Beklenen: '{expected_part}', Mevcut: '{current_url}'"
            )

    def js_click(self, locator):
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(locator)
        )
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.driver.execute_script("window.scrollBy(0, -100);")
        self.driver.execute_script("arguments[0].click();", element)

    def safe_click(self, locator, timeout=30, scroll=True):
        wait = WebDriverWait(self.driver, timeout)
        # 1) İlk bekleme
        element = wait.until(EC.presence_of_element_located(locator))
        # 2) Scroll
        if scroll:
            self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", element)
            self.driver.execute_script("window.scrollBy(0, -120);")
        # 3) Clickable bekle (overlay/animasyon için)
        element = wait.until(EC.element_to_be_clickable(locator))
        # 4) Normal click dene, intercept olursa JS fallback + retry
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            element = wait.until(EC.presence_of_element_located(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def element_count(self, locator, timeout=30):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return len(self.driver.find_elements(*locator))

    def wait_for_url_to_be(self, expected_url: str, timeout=30):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(expected_url)
        )

    def get_titles(self, locator, timeout=20):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.driver.find_elements(*locator)
