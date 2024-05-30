import unittest
from selenium import webdriver
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.qa_careers_page import QACareersPage

class TestScenario(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_scenario(self):
        # Anasayfa erişimi doğruluğu
        home_page = HomePage(self.driver)
        home_page.driver.get(home_page.url)
        self.assertTrue(home_page.verify_homepage_accessibility(), "Anasayfaya erişilemiyor.")
        
        # Kariyer sayfası erişimi ve doğruluğu
        careers_page = CareersPage(self.driver)
        careers_page.go_to_career_page()
        self.assertTrue(careers_page.verify_career_page_accessibility(), "Kariyer sayfasına erişilemiyor.")
        
        # QA kariyer sayfası erişimi
        qa_careers_page = QACareersPage(self.driver)
        qa_careers_page.driver.get(qa_careers_page.url)
        
        # Tüm QA işlerini gör
        qa_careers_page.click_see_all_qa_jobs()
        
        # İşleri filtreleme
        qa_careers_page.filter_jobs(location="Istanbul, Turkey", department="Quality Assurance")

        self.driver.execute_script("window.scrollTo(0, 500);")
        
        # Listelenen işlerin görünürlüğü ve iş detaylarının doğruluğu
        self.assertTrue(qa_careers_page.visibility_of_jobs(), "İşler listelenemedi.")
        self.assertTrue(qa_careers_page.verify_job_details(), "İş detayları doğrulanamadı.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
