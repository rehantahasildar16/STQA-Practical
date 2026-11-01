from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

#Implicit Wait tells Selenium to wait for a certain amount of time while searching for every element before throwing an error.

# Implicit Wait
driver.implicitly_wait(10)

# Open Practice Form
driver.get("https://demoqa.com/automation-practice-form")

# ----------------------------------------------------
# USER MANUALLY FILLS THE FORM
# ----------------------------------------------------
print("Please enter the following details manually:")
print("1. First Name")
print("2. Last Name")
print("3. Date of Birth")
input("After completing these fields, press Enter to continue...")

# ----------------------------------------------------
# AUTOMATION STARTS HERE
# ----------------------------------------------------

# Select Gender
driver.find_element(By.XPATH, "//label[text()='Female']").click()

# Select Sports Checkbox
driver.find_element(By.XPATH, "//label[text()='Sports']").click()

#Definition
#Explicit Wait tells Selenium to wait for one specific element or condition before performing the next action.

# Explicit Wait
wait = WebDriverWait(driver, 10)

# Select State
driver.find_element(By.ID, "state").click()

state = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='NCR']"))
)
state.click()

# Open Alerts Page
driver.get("https://demoqa.com/alerts")

# Click Alert Button
driver.find_element(By.ID, "alertButton").click()

# Wait for Alert
alert = wait.until(EC.alert_is_present())

print("Alert Text:", alert.text)

# Click OK
alert.accept()

# Open Frames Page
driver.get("https://demoqa.com/frames")

# Switch to Frame
wait.until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
)

# Print Frame Text
print("Frame Text:", driver.find_element(By.ID, "sampleHeading").text)

# Return to Main Page
driver.switch_to.default_content()

# Close Browser
driver.quit()