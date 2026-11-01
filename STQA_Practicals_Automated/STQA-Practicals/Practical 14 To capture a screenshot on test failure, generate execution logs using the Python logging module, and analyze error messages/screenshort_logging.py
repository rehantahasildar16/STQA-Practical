from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
import time
import os

# Create Logging File
logging.basicConfig(
    filename="execution.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

logging.info("========== TEST STARTED ==========")

# Launch Browser
driver = webdriver.Chrome()

driver.maximize_window()

# Change this path according to your computer
driver.get(Path(__file__).with_name("login.html").resolve().as_uri())

logging.info("Browser Opened")

time.sleep(5)

# Enter Username
driver.find_element(By.ID, "username").send_keys("admin")
logging.info("Username Entered")

time.sleep(3)

# Enter Wrong Password (Intentional Failure)
driver.find_element(By.ID, "password").send_keys("1111")
logging.info("Password Entered")

time.sleep(3)

# Click Login Button
driver.find_element(By.TAG_NAME, "button").click()

logging.info("Login Button Clicked")

time.sleep(5)

# Read Message
message = driver.find_element(By.ID, "msg").text

print("Result :", message)

logging.info("Message Received : " + message)

# Validation
if message == "Login Successful":

    print("Test Passed")

    logging.info("Login Test Passed")

else:

    print("Test Failed")

    logging.error("Login Test Failed")

    # Screenshot
    screenshot_name = "login_failed.png"

    driver.save_screenshot(screenshot_name)

    print("Screenshot Saved")

    logging.info("Screenshot Saved : " + screenshot_name)

time.sleep(5)

driver.quit()

logging.info("Browser Closed")

logging.info("========== TEST COMPLETED ==========")

logging.shutdown()

print("\nProgram Completed Successfully")

print("Current Folder :", os.getcwd())