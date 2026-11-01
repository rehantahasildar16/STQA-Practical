from pathlib import Path
import csv, os, subprocess, sys, webbrowser

ROOT = Path(__file__).resolve().parent

def find_dir(prefix):
    matches = [p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(prefix)]
    if not matches:
        raise FileNotFoundError("Folder not found: " + prefix)
    return matches[0]

def run_script(folder_prefix, script_name):
    folder = find_dir(folder_prefix)
    script = folder / script_name
    if not script.exists():
        print("Required script not found:", script)
        return
    print("\\nRunning:", script.name)
    result = subprocess.run([sys.executable, str(script)], cwd=str(folder))
    print("\\nProcess exit code:", result.returncode)

def open_csv():
    folder=find_dir("Practical 3")
    file=folder/"Combined_STLC_Process.csv"
    print("CSV:", file)
    try: os.startfile(str(file))
    except AttributeError: webbrowser.open(file.as_uri())

def practical7():
    print("\\n1. Display 10 student records from CSV")
    print("2. Update 10 records: Course = MCA (creates updated CSV)")
    choice=input("Select: ").strip()
    if choice=="1": run_script("Practical 7", "Practical d 7.py")
    elif choice=="2": run_script("Practical 7", "STQA Practical c 7.py")
    else: print("Invalid choice")

def run_pytest():
    folder=find_dir("Practical 16")
    script=folder/"test_login1.py"
    if not script.exists():
        print("Pytest file not found")
        return
    report=ROOT/"STQA_Test_Report.html"
    subprocess.run([sys.executable,"-m","pytest",str(script),"-v","--html",str(report),"--self-contained-html"],cwd=str(folder))
    print("HTML report:", report)
    if report.exists(): webbrowser.open(report.as_uri())

def grid_practical(prefix, script):
    url=input("Selenium Grid URL [http://localhost:4444]: ").strip() or "http://localhost:4444"
    os.environ["SELENIUM_GRID_URL"]=url
    run_script(prefix,script)

def locust():
    folder=find_dir("Added new practicals folder")
    script=next(folder.rglob("load_test.py"),None)
    if not script: print("Locust script not found"); return
    host=input("Target website URL (example https://example.com): ").strip()
    if not host.startswith(("http://","https://")):
        print("Please enter a valid http/https URL."); return
    subprocess.run([sys.executable,"-m","locust","-f",str(script),"--host",host],cwd=str(script.parent))

MENU=[
("3","Practical 3 - Test plan / scenarios / test cases (open CSV)",open_csv),
("4","Practical 4 - Selenium Grid (needs running Grid server)",lambda:grid_practical("Practical 4","grid_test.py")),
("5","Practical 5 - Login automation (internet required)",lambda:run_script("Practical 5","login_test.py")),
("6","Practical 6 - Web element interaction",lambda:run_script("Practical 6","web_element_interaction.py")),
("7","Practical 7 - Student CSV records",practical7),
("8","Practical 8 - Marksheet extraction and score analysis",lambda:run_script("Practical 8","Marksheet.py")),
("9","Practical 9 - Count web page objects (internet required)",lambda:run_script("Practical 9","object_count.py")),
("10","Practical 10 - Dropdown testing (internet required)",lambda:run_script("Practical 10","dropdown.py")),
("11","Practical 11 - Checkbox testing",lambda:run_script("Practical 11","checkbox_Practical 11.py")),
("12","Practical 12 - Dynamic web table / sorting",lambda:run_script("Practical 12","dynamic_web_table.py")),
("13","Practical 13 - File upload / download",lambda:run_script("Practical 13","file_upload_download.py")),
("14","Practical 14 - Screenshot and logging",lambda:run_script("Practical 14","screenshort_logging.py")),
("15","Practical 15 - Page Object Model (POM)",lambda:run_script("Practical 15","for run 2.py")),
("16","Practical 16 - Pytest + HTML report",run_pytest),
("17","Practical 17 - Jenkins Selenium script (local demo)",lambda:run_script("Practical 17","login_test3.py")),
("18","Cross-browser testing using Selenium Grid",lambda:grid_practical("Added new practicals folder","cross_browser_test.py")),
("19","Load testing using Locust (target URL required)",locust),
]

def main():
    while True:
        print("\\n"+"="*64)
        print("             STQA PRACTICAL AUTOMATION MENU")
        print("="*64)
        for key,label,_ in MENU: print(f" {key:>2}. {label}")
        print("  0. Exit")
        print("="*64)
        choice=input("Select practical number: ").strip()
        if choice=="0": print("Thank you!"); break
        item=next((x for x in MENU if x[0]==choice),None)
        if not item: print("Invalid selection. Try again."); continue
        try: item[2]()
        except KeyboardInterrupt: print("\\nStopped by user.")
        except Exception as e: print("\\nERROR:",type(e).__name__,e)
        input("\\nPress Enter to return to menu...")

if __name__=="__main__": main()
