from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage

class QACareersPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://useinsider.com/careers/quality-assurance/"
    
    def click_see_all_qa_jobs(self):
        self.close_cookies()
        see_all_qa_jobs_btn = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='page-head']/div/div/div[1]/div/div/a")))
        self.driver.execute_script("arguments[0].click();", see_all_qa_jobs_btn)
    
    def filter_jobs(self, location, department):
        self.close_cookies() 
        location_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='select2-filter-by-location-container']")))
        location_dropdown.click()
        
        location_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[text()='{location}']")))
        location_option.click()
        
        department_dropdown = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//*[@id='select2-filter-by-department-container']")))
        department_dropdown.click()
        
        department_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//li[text()='{department}']")))
        department_option.click()
    
    def visibility_of_jobs(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']")))
            return True
        except:
            return False
    
    def verify_job_details(self):
        try:
            job_elements = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='jobs-list']"))
            )
            
            for job_element in job_elements:
                position_department_element = WebDriverWait(job_element, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']/div[1]/div/span"))
                )
                location_element = WebDriverWait(job_element, 10).until(
                    EC.visibility_of_element_located((By.XPATH, "//*[@id='jobs-list']/div[1]/div/div"))
                )
                
                position_department_text = position_department_element.text
                location_text = location_element.text
                
                if "Quality Assurance" not in position_department_text:
                    return False
                if "Istanbul, Turkey" not in location_text:
                    return False
            
            return True
        except:
            return False
