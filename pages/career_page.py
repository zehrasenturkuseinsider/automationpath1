import driver
from selenium.webdriver.common.by import By
from config.config import Config
from pages.base_page import BasePage
import time
class CareerPage(BasePage):

    # Locators
    SEE_ALL_TEAMS = (By.XPATH,"//a[@class='inso-btn see-more']")
    LOCATION_TABS = (By.XPATH, "//*[@id='page-wrapper']/div/div[4]/div/div/div/div/div[2]")
    RIGHT_ARROW = (By.XPATH, "//div[@class='insiderone-locations-slider-header-right']//a[@aria-label='Next slide']")
    LEFT_ARROW = (By.XPATH, "//div[@class='insiderone-locations-slider-header-right']//a[@aria-label='Previous slide']")

    SLIDER_ROOT = (By.CSS_SELECTOR, ".insiderone-locations-slider-container")
    SLIDES_ALL = (By.CSS_SELECTOR, ".insiderone-locations-slider-container .swiper-slide")  # tüm kartlar
    SLIDES_VISIBLE = (By.CSS_SELECTOR, ".insiderone-locations-slider-container .swiper-slide-active, "
                                       ".insiderone-locations-slider-container .swiper-slide-next, "
                                       ".insiderone-locations-slider-container .swiper-slide-prev")

    ICON_CARD_BUTTONS = (
        By.CLASS_NAME,
        "insiderone-icon-cards-grid-item-btn"
    )

    def __init__(self, driver):
        super().__init__(driver)

    def verify_career_page_opened(self):
        self.verify_url(Config.CAREER_PAGE)

    def see_all_teams_and_verify_team_cards(self):
        self.scroll_to_element(self.LOCATION_TABS)
        self.js_click(self.SEE_ALL_TEAMS)

    def get_location_tab_count(self):
        self.wait_element_presence(self.SLIDER_ROOT)
        print(len(self.driver.find_elements(*self.SLIDES_ALL)))
        return len(self.driver.find_elements(*self.SLIDES_ALL))


    def click_right_arrow(self):
        self.safe_click(self.RIGHT_ARROW)

    def click_left_arrow(self):
        self.safe_click(self.LEFT_ARROW)

    def swipe_locations_to_right(self):
        tab_count = self.get_location_tab_count()

        for i in range(tab_count):
            self.click_right_arrow()
            time.sleep(1)

    def swipe_locations_to_left(self):
        tab_count = self.get_location_tab_count()

        for i in range(tab_count):
            self.click_left_arrow()
            time.sleep(1)

    def click_icon_card_by_index(self, index: int):
        self.click_by_index_safe(self.ICON_CARD_BUTTONS, index)

