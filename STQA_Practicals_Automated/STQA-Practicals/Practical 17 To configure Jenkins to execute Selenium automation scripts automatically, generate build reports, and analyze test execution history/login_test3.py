from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(Path(__file__).with_name("login.html").resolve().as_uri())

print("Browser Opened")
time.sleep(3)

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("1234")

print("Username and Password Entered")
time.sleep(2)

driver.find_element(By.TAG_NAME, "button").click()
print("Login Button Clicked")

time.sleep(3)
result = driver.find_element(By.ID, "msg").text
print("Result :", result)

if result == "Login Successful":
    print("Test Passed")
else:
    print("Test Failed")

time.sleep(5)
driver.quit()
print("Browser Closed")