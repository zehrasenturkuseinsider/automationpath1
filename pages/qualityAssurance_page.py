from selenium.webdriver.common.by import By
from config.config import Config
from pages.base_page import BasePage

class QualityAssurancePage(BasePage):

    #Locators
    FILTER_BAR = (By.CLASS_NAME, "filter-bar")
    LOCATION_DRPDWN = (By.CSS_SELECTOR, ".filter-button-wrapper.filter-button-wrapper-margin-right")
    LOCATION_ISTANBUL = (By.XPATH, "//a[normalize-space()='Istanbul, Turkiye']")
    LOCATION_CHECK = (By.CSS_SELECTOR, ".small-category-label.location")
    JOB_TITLES = (By.CLASS_NAME, "posting-title")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = Config.QA_URL

    def verify_qa_page_opened(self):
        self.wait_for_url_to_be(Config.QA_URL)
        current_url = self.get_current_url()
        assert current_url == Config.QA_URL, (
            f"Quality Assurance page was not opened. "
            f"Expected: {Config.QA_URL} | Actual: {current_url}"
        )

    def click_location_dropdown(self, index: int):
        self.click_by_index_safe(self.LOCATION_DRPDWN, index)

    def select_location_dropdown(self):
        self.safe_click(self.LOCATION_ISTANBUL)

    def verify_all_jobs_are_quality_assurance(self):
        job_titles = self.get_titles(self.JOB_TITLES)
        assert job_titles, "No job postings found!"

        for job in job_titles:
            title_text = job.text.strip()
            assert "Quality Assurance" in title_text, \
                f"Unexpected job title found: {title_text}"

    def verify_all_location_are_istanbul(self):
        location = self.get_titles(self.LOCATION_CHECK)
        assert location, "No job postings found!"

        for location in location:
            location_details = location.text.strip()
            assert "ISTANBUL, TURKIYE" in location_details, \
                f"Unexpected job title found: {location_details}"
