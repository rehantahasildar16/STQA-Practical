from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get(Path(__file__).with_name("Marksheet.html").resolve().as_uri())
driver.maximize_window()
time.sleep(2)

rows = driver.find_elements(By.XPATH, "//table//tr[position()>1]")

total_students = len(rows)
above_60 = 0

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "td")
    name = cols[0].text
    maths = int(cols[1].text)
    science = int(cols[2].text)
    english = int(cols[3].text)

    print(name, maths, science, english)

    if maths > 60 or science > 60 or english > 60:
        above_60 += 1

percentage = (above_60 / total_students) * 100

print("\n---------------------------")
print("Total Students :", total_students)
print("Students Above 60 :", above_60)
print("Percentage :", percentage, "%")

driver.quit()