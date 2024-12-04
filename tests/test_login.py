import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import LoginPage
import time

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.login_page = LoginPage(cls.driver)


    def test_empty_credentials(self):
        """Test error message for empty username and password"""
        self.login_page.open_login_page()
        self.login_page.enter_username("")
        self.login_page.enter_password("")
        self.login_page.click_login()
        error_message = self.login_page.get_error_message()
        time.sleep(3)
        print("Error message for empty credentials:", error_message)
        self.assertEqual(error_message, "Required")

    def test_invalid_credentials(self):
        """Test error messages for invalid usernames and passwords"""
        self.login_page.open_login_page()
        self.login_page.enter_username("123abc")
        self.login_page.enter_password("456def")
        self.login_page.click_login()
        error_message = self.login_page.get_error_message()
        time.sleep(3)
        print("Error message for invalid credentials:", error_message)
        self.assertEqual(error_message, "Invalid credentials")

    def test_valid_credentials(self):
        """Test the login functionality with the correct username and password"""
        self.login_page.open_login_page()
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()
        expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        time.sleep(3)
        self.assertEqual(self.driver.current_url, expected_url)
        print("Login successful, redirected to:", self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
