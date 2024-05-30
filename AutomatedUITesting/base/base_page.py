from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def close_cookies(self):
        try:
            cookies = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located((By.ID, "wt-cli-accept-all-btn")))
            cookies.click()
        except:
            pass
