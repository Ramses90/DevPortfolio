from selenium import webdriver
import unittest

class MywebTest(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):        
        cls.driver = webdriver.Chrome(executable_path='../drivers/chromedriver')
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
    
    def test_serach(self):
        self.driver.get("https://selenium-python.readthedocs.io/faq.html")
        self.driver.find_element_by_name("q").send_keys("Serach for my name")
        self.driver.find_element_by_name("btnk").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def test_serach2(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("Serach for my name")
        self.driver.find_element_by_name("btnk").click()

    @classmethod
    def tearDownClass(cls): 
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")
