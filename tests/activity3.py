import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestWebApp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_fill_form(self):
        driver = self.driver
        driver.get("https://qavalidation.com/demo-form/?contact-form-hash=875a4285a37d67e2416c29f39cb2425c0d8d255c")
        driver.find_element(By.NAME, "g4072-fullname").send_keys("John Doe")
        driver.find_element(By.NAME, "g4072-email").send_keys("john.doe@example.com")
        driver.find_element(By.NAME, "g4072-phonenumber").send_keys("3402567891")
        driver.find_element(By.NAME, "g4072-otherdetails").send_keys("This is a test message.")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        sleep(3)
        success_message = driver.find_element(By.ID, "contact-form-success-header").text
        self.assertIn("Your message has been sent", success_message)

    def test_extract_information(self):
        driver = self.driver
        driver.get("https://www.jenkins.io/")
        info = driver.find_element(By.XPATH, "//h1").text
        self.assertIn("Jenkins", info)

    def test_login(self):
        driver = self.driver
        driver.get("https://demo.guru99.com/test/login.html")
        driver.find_element(By.NAME, "email").send_keys("user@example.com")
        driver.find_element(By.NAME, "passwd").send_keys("password")
        driver.find_element(By.ID, "SubmitLogin").click()
        sleep(2)
        success_message = driver.find_element(By.CSS_SELECTOR, "h3").text
        self.assertIn("Successfully Logged in...", success_message)

    def test_search(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium")
        search_box.send_keys(Keys.RETURN)
        sleep(2)
        results = driver.find_elements(By.CLASS_NAME, "g")
        self.assertGreater(len(results), 0)

    def test_navigation(self):
        driver = self.driver
        driver.get("https://www.w3schools.com/")
        driver.find_element(By.LINK_TEXT, "PYTHON").click()
        sleep(3)
        universe_text = driver.find_element(By.CSS_SELECTOR, "h1").text
        self.assertIn("Python Tutorial", universe_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()