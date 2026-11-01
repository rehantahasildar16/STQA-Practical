from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

driver = webdriver.Chrome()

driver.get(Path(__file__).with_name("file_upload.html").resolve().as_uri())

driver.maximize_window()

time.sleep(5)

# Upload File

filepath = str(Path(__file__).with_name("upload_sample.txt").resolve())

driver.find_element(By.ID,"file").send_keys(filepath)

time.sleep(5)

driver.find_element(By.XPATH,"//button[text()='Upload']").click()

time.sleep(5)

message = driver.find_element(By.ID,"msg").text

print("Upload Status :",message)

# Download File

driver.find_element(By.XPATH,"//button[text()='Download']").click()

print("Downloading File...")

time.sleep(10)

download_path = str(Path(__file__).with_name("sample.txt").resolve())

if os.path.exists(download_path):

    print("Download Successful")

else:

    print("Download Failed")

time.sleep(5)

driver.quit()