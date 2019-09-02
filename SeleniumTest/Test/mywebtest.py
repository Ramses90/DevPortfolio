from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium import webdriver
import unittest
import HtmlTestRunner


class MywebTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path='/Users/ramsesmachado/Documents/DevPortfolio/DevPortfolio/DevPortfolio/SeleniumTest/drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search(self):
        self.driver.get(
            "http://18.218.65.248:8000/")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_search3(self):
        self.driver.get("http://18.218.65.248:8000/")
        self.driver.find_element_by_link_text("#about").click()
        self.driver.find_element_by_name("About").click()


    def test_serach2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("DevPortFolio")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='SeleniumTest/reports'))

#pip install html-testRunner

