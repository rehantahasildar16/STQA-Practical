import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
driver = webdriver.Remote(
   command_executor=os.environ.get("SELENIUM_GRID_URL", "http://localhost:4444"),
   options=options
)
driver.get("https://www.google.com")
print("Page Title:", driver.title)
driver.quit()
