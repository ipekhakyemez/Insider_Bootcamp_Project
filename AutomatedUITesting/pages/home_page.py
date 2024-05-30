from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/"

    def verify_homepage_accessibility(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "container-fluid")))
            return True
        except:
            return False
