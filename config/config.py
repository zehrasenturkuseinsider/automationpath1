import os
class Config:
    """Project configuration"""

    # Base URLs
    BASE_URL = "https://insiderone.com/"

    # Timeouts (seconds)
    IMPLICIT_WAIT = 10
    EXPLICIT_WAIT = 15
    PAGE_LOAD_TIMEOUT = 30

    # Browser
    BROWSER = "chrome"
    HEADLESS = os.getenv("HEADLESS", "False") == "True"

    # Career Page
    CAREER_PAGE = "https://insiderone.com/careers/"
    QA_URL = "https://jobs.lever.co/insiderone?team=Quality%20Assurance"
