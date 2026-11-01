from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_website():

    driver = webdriver.Chrome()

    driver.maximize_window()

    driver.get("https://demoqa.com/login")

    # URL Validation
    assert "login" in driver.current_url

    print("Website Opened Successfully")

    driver.quit()


def test_page_title():

    driver = webdriver.Chrome()

    driver.get("https://demoqa.com/login")

    # Title Validation
    assert driver.title != ""

    print("Title Verified Successfully")

    driver.quit()