from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import shutil
from openpyxl import load_workbook
import requests
import time

input_curl = []

# chromedriver 찾기
driver_directory = os.path.dirname(os.path.abspath(__file__))

# 나중에 쓸 class_time 변수
class_time = input("해당 학생은 하루에 총 몇 시간 수업하나요?(시간 단위로 입력해주세요):\n")

print("cURL을 입력하고 엔터를 두번 눌러주세요:")

while True:
    line = input()
    if line == "":
        break
    input_curl.append(line)

input_curl = '\n'.join(input_curl)

# translated_output에 있는 변수 사전 생성(이후 에러 생겨서 미리 생성)
response = ()
cookies = {}
headers = {}

# 로딩 오래 걸려서 로딩중
print("로딩중...")

webdriver_path = "r'" + driver_directory + "'"

# 컬 to 파이썬 컨버터(웹페이지)에서 변환기 가져오기
url = 'https://curlconverter.com/'

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

input_box = driver.find_element(By.ID, 'curl-code')
output_box = driver.find_element(By.ID, 'generated-code')

input_box.send_keys(input_curl)

translated_output = output_box.text

# 출력된 translated_output: cookies={} header={} param={}
try:
    exec(translated_output)
except Exception as e:
    print("Error", e)

# 수업 내용 호출을 위한 soup
soup_class = BeautifulSoup(response.text, 'html.parser')

# 학생 정보 호출을 위한 header 및 response 변경
new_url = headers['Referer']
new_referer = 'http://erp.livedu.co/manage/student/student.php'

headers['Referer'] = new_referer

# 학생 정보 호출
new_response = requests.get(
    new_url,
    cookies=cookies,
    headers=headers,
    verify=False,
)

# 학생 정보를 위한 soup
soup_student = BeautifulSoup(new_response.text, 'html.parser')

driver.quit()

data_class = soup_class.select('body > table > tr:nth-child(3) > td > form > table:nth-child(4) div')
data_student = soup_student.select('body > table > tr:nth-child(3) > td > form > table div')

# 읽는 그대로
student_name = []
teacher_name = []
student_grade = []
student_subject = []

for index_student, tag_student in enumerate(data_student[14:], 1):
    if index_student == 3:
        student_subject.append(tag_student.contents[0])
    if index_student == 4:
        student_name.append(tag_student.contents[0])
    if index_student == 6:
        student_grade.append(tag_student.contents[0])

dates = []  # 수업 일자
class_content = []  # 수업 범위
homework = []  # 숙제 범위
hw_achievement = []  # 숙제 달성도
study = []  # 수업 소견

for index, tag in enumerate(data_class[11:], 1):
    if index == 3:
        teacher_name.append(tag.contents[0])

    if index % (11 * int(class_time)) == 4:
        dates.append(tag.contents[0])

    if index % (11 * int(class_time)) == 0 and index > 21:
        study.append(tag.contents[10][18:])
    if index % (11 * int(class_time)) == 0 and index > 21:
        homework.append(tag.contents[8][12:])
    if index % (11 * int(class_time)) == 0 and index > 21:
        hw_achievement.append(tag.contents[6][17:])

    if index == 11:  # 첫줄만 에러 떠서 별도 지정
        inner = tag.contents[1].text
        x = inner.splitlines()[5]  # 수업 소견
        study.append(x[16:])
        y = inner.splitlines()[4]  # 숙제
        homework.append(y[10:])
        z = inner.splitlines()[3]  # 숙제 달성도
        hw_achievement.append(z[15:])

    if index % (11 * int(class_time)) == 10:
        class_content.append(tag.contents[0])

dates.reverse()
study.reverse()
class_content.reverse()
homework.reverse()
hw_achievement.reverse()

# 총 수업 시간
total_time = len(dates) * int(class_time) * 60

# 월말보고서 불러오기, 완성된 엑셀은 '완성소견서'
shutil.copy("소견서.xlsx", "완성소견서.xlsx")
file_source = "완성소견서.xlsx"

workbook = load_workbook(filename=file_source)

ws = workbook["월말소견서"]


# 입력기 함수
def enter_cell(a, b, component):
    ws.cell(row=a, column=b).value = component


# 총 수업시간 입력
enter_cell(12, 12, str(total_time))
# 학생 이름, 학년, 선생님 이름, 과목 입력
enter_cell(6, 2, student_name[0])
enter_cell(6, 12, student_grade[0])
enter_cell(12, 2, teacher_name[0])
enter_cell(12, 3, student_subject[0])

# 나머지 입력, count에 따라 순서대로
count = 0
while count < len(dates):
    count_a = int(17+7*count)
    enter_cell(count_a, 2, dates[count])
    enter_cell(count_a, 3, int(class_time)*60)
    enter_cell(count_a, 5, class_content[count])
    enter_cell(count_a, 16, hw_achievement[count])
    enter_cell(count_a+2, 3, homework[count])
    enter_cell(count_a+4, 3, study[count])
    count += 1

workbook.save(filename=file_source)

print("완료되었습니다. 3...", end=''), time.sleep(1), print("2...", end=''), time.sleep(1), print("1...", end='')
