import time
import pytest
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
from pages.career_page import CareerPage
from config.config import Config
from pages.qualityAssurance_page import QualityAssurancePage


class TestautomationPath1:
    @pytest.mark.smoke
    def test_insider_career_flow(self, driver):
        home_page = HomePage(driver)
        home_page.accept_cookies()
        home_page.homepage_verify()
        home_page.go_to_career_page()

        career_page = CareerPage(driver)
        career_page.verify_career_page_opened()
        career_page.see_all_teams_and_verify_team_cards()
        career_page.swipe_locations_to_right()
        career_page.swipe_locations_to_left()
        career_page.click_icon_card_by_index(8)
        time.sleep(5)

        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.verify_qa_page_opened()
        quality_assurance_page.click_location_dropdown(1)
        quality_assurance_page.select_location_dropdown()
        time.sleep(5)
        quality_assurance_page.verify_all_jobs_are_quality_assurance()
        quality_assurance_page.verify_all_location_are_istanbul()



