from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Launch Chrome
driver = webdriver.Chrome()

# Maximize Browser
driver.maximize_window()

# Open Website
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter Username
driver.find_element(By.ID, "username").send_keys("student")

# Enter Password
driver.find_element(By.ID, "password").send_keys("Password123")

# Click Login
driver.find_element(By.ID, "submit").click()

# Wait for page
time.sleep(3)

# -----------------------------
# Validation 1 : URL Validation
# -----------------------------

expected_url = "https://practicetestautomation.com/logged-in-successfully/"

actual_url = driver.current_url

assert actual_url == expected_url

print("URL Validation Passed")

# ------------------------------------
# Validation 2 : Welcome Message Check
# ------------------------------------

welcome = driver.find_element(By.TAG_NAME, "h1").text

assert welcome == "Logged In Successfully"

print("Welcome Message Validation Passed")

# ---------------------------------
# Validation 3 : Logout Visibility
# ---------------------------------

logout = driver.find_element(By.LINK_TEXT, "Log out")

assert logout.is_displayed()

print("Logout Button is Visible")

print("Login Successful")

time.sleep(5)

driver.quit()