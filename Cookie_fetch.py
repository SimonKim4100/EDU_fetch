from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import pandas as pd
from openpyxl import load_workbook

driver_directory = os.path.dirname(os.path.abspath(__file__))
webdriver_path = "r'" + driver_directory + "'"
url2 = 'http://erp.livedu.co/manage/student/student.php'
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url2)
get_student = driver.find_element(By.ID, 'st_name')
name = get_student.get_attribute("value")
print(name)

driver.quit()




http://erp.livedu.co/manage/student/student.php

http://erp.livedu.co/manage/student/student_info.inc_attendance.php?st_no=301

#listDiv > table:nth-child(9) > tbody > tr:nth-child(2) > td:nth-child(1) > div > a
body > table > tbody > tr:nth-child(3) > td > form > table > tbody > tr:nth-child(3) > td:nth-child(4) > div