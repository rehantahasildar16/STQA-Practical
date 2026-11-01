from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def test_browser(browser_name):

    # Select browser
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()

    else:
        print("Invalid browser:", browser_name)
        return

    start_time = time.time()

    driver = None

    try:
        # Connect to Selenium Grid
        driver = webdriver.Remote(
            command_executor=os.environ.get("SELENIUM_GRID_URL", "http://localhost:4444"),
            options=options
        )

        # Open Google
        driver.get("https://www.google.com")

        print(browser_name, "Title:", driver.title)

        # Find search box
        search_box = driver.find_element(By.NAME, "q")

        # Enter text
        search_box.send_keys("Selenium WebDriver")

        time.sleep(2)

        print(browser_name, "Test Passed")

    except Exception as e:
        print(browser_name, "Test Failed")
        print("Error:", e)

    finally:
        if driver:
            driver.quit()

    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time

    print(browser_name,
          "Execution Time:",
          round(execution_time, 2),
          "seconds")

    print("--------------------------------")


# Run test on Chrome
test_browser("chrome")

# Run test on Firefox
test_browser("firefox")

# Run test on Edge
test_browser("edge")