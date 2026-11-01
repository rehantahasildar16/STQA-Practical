from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get(Path(__file__).with_name("checkbox.html").resolve().as_uri())

driver.maximize_window()

time.sleep(2)

checkboxes = driver.find_elements(By.NAME,"subject")

print("Total Checkboxes :",len(checkboxes))

checked=0
unchecked=0

for cb in checkboxes:
    if cb.is_selected():
        checked=checked+1
    else:
        unchecked=unchecked+1

print("Checked :",checked)
print("Unchecked :",unchecked)

subjects=["Python","Java","C++","DBMS","Operating System","CN","Software Engineering"]

print("\nSubjects")

for i in range(len(subjects)):
    print(i+1,".",subjects[i])

choice=input("\nEnter subject numbers (Example 1,3,5): ")

numbers=choice.split(",")

for num in numbers:

    index=int(num)-1

    if index>=0 and index<len(checkboxes):

        if not checkboxes[index].is_selected():

            checkboxes[index].click()

print("\nSelected Subjects")

for i in range(len(checkboxes)):
    if checkboxes[i].is_selected():
        print(subjects[i])

driver.find_element(By.XPATH,"//input[@type='submit']").click()

time.sleep(2)

message=driver.find_element(By.ID,"msg").text

print("\n",message)

time.sleep(5)

driver.quit()