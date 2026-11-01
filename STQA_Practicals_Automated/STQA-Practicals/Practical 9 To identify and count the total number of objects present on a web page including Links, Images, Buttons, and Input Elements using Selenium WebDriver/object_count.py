from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.wikipedia.org")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
images = driver.find_elements(By.TAG_NAME, "img")
buttons = driver.find_elements(By.TAG_NAME, "button")
inputs = driver.find_elements(By.TAG_NAME, "input")

print("========== Object Count ==========")
print("Total Links :", len(links))
print("Total Images :", len(images))
print("Total Buttons :", len(buttons))
print("Total Input Elements :", len(inputs))
print("----------------------------------")
print("Total Objects :", len(links) + len(images) + len(buttons) + len(inputs))

time.sleep(10)

driver.quit()