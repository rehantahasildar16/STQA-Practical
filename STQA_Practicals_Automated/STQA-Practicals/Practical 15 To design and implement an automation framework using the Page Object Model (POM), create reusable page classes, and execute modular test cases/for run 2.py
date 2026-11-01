from pathlib import Path
import unittest
import time
from selenium import webdriver
from login_page import LoginPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        self.driver.get(Path(__file__).with_name("login.html").resolve().as_uri())

        time.sleep(3)

    def test_login(self):

        login = LoginPage(self.driver)

        login.enter_username("admin")

        time.sleep(2)

        login.enter_password("1234")

        time.sleep(2)

        login.click_login()

        time.sleep(3)

        result = login.get_message()

        print("Result :", result)

        self.assertEqual(result, "Login Successful")


   
    def test_homepage(self):
        print("Homepage test executed")


    def tearDown(self):

        time.sleep(5)

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()