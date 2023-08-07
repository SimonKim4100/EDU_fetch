from selenium import webdriver
from bs4 import BeautifulSoup
import requests

cookies = {
    'f33d2ed86bd82d4c22123c9da444d8ab': 'MTY4NDkzMTIwNQ%3D%3D',
    '96b28b766b7e0699aa91c9ff3d890663': 'aHR0cDovL2VycC5saXZlZHUuY28vbWFuYWdlLw%3D%3D',
    '8a5d10ae2727b4ee0a7694ad9a3ac9e9': 'dGVhY2hlcg%3D%3D',
    'f5b70989e6e9268d600366f7ae77c01a': 'MQ%3D%3D',
    'al': 'KR',
    '_ga': 'GA1.1.1049943602.1688712638',
    '_fbp': 'fb.1.1688712638155.26382194',
    '_ga_CXVE0LEQ0N': 'GS1.1.1688712638.1.1.1688713044.60.0.0',
    'PHPSESSID': 'oja452prceti8cg98qev2eqfd3',
    '2a0d2363701f23f8a75028924a3af643': 'MjE4LjE1My4xNDQuMTg0',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,en-GB;q=0.6',
    'Connection': 'keep-alive',
    # 'Cookie': 'f33d2ed86bd82d4c22123c9da444d8ab=MTY4NDkzMTIwNQ%3D%3D; 96b28b766b7e0699aa91c9ff3d890663=aHR0cDovL2VycC5saXZlZHUuY28vbWFuYWdlLw%3D%3D; 8a5d10ae2727b4ee0a7694ad9a3ac9e9=dGVhY2hlcg%3D%3D; f5b70989e6e9268d600366f7ae77c01a=MQ%3D%3D; al=KR; _ga=GA1.1.1049943602.1688712638; _fbp=fb.1.1688712638155.26382194; _ga_CXVE0LEQ0N=GS1.1.1688712638.1.1.1688713044.60.0.0; PHPSESSID=oja452prceti8cg98qev2eqfd3; 2a0d2363701f23f8a75028924a3af643=MjE4LjE1My4xNDQuMTg0',
    'If-Modified-Since': 'Mon, 07 Aug 2023 09:00:53 GMT',
    'Referer': 'http://erp.livedu.co/manage/student/student_info.inc_schedule.php?st_no=301',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

params = {
    'st_no': '301',
}

response = requests.get(
    'http://erp.livedu.co/manage/student/student_info.inc_attendance.php',
    params=params,
    cookies=cookies,
    headers=headers,
    verify=False,
)

soup = BeautifulSoup(response.content, 'html.parser')

data = soup.select_one('body > table > tbody > tr:nth-child(3) > td > form > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(3) > div').text

print(data)

# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Chrome()

# url = 'http://erp.livedu.co/manage/student/student.php'

# driver.get(url)

# driver.implicitly_wait(10)

# iframe_element = driver.find_element('body > table > tbody > tr:nth-child(1) > td > table > tbody > tr:nth-child(2)
# > ' 'td > table > tbody > tr:nth-child(3) > td > table > tbody > tr > td:nth-child(' '2) > table > tbody >
# tr:nth-child(3) > td > iframe') driver.switch_to.frame(iframe_element)

# iframe_html = driver.page_source
# iframe_soup = BeautifulSoup(iframe_html, 'html_parser')

# data = iframe_soup.select_one('body > table > tbody > tr:nth-child(3) > td > form > table:nth-child(4) > tbody > '
# 'tr:nth-child(3) > td:nth-child(3) > div').text

# print(data)
