from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class CareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    def go_to_career_page(self):
        company_menu = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(), 'Company')]")))
        company_menu.click()
        career_link = WebDriverWait(self.driver,20).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Careers')]")))
        career_link.click()

    def verify_career_page_accessibility(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='career-our-location']/div/div/div")))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='career-find-our-calling']/div/div/div[2]")))
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/section[4]/div/div/div")))
            return True
        except:
            return False
