from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "username")
    password = (By.ID, "password")
    login_btn = (By.TAG_NAME, "button")
    message = (By.ID, "msg")

    def enter_username(self, uname):
        self.driver.find_element(*self.username).send_keys(uname)

    def enter_password(self, pwd):
        self.driver.find_element(*self.password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(*self.login_btn).click()

    def get_message(self):
        return self.driver.find_element(*self.message).text