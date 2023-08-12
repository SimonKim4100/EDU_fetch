# EDU_fetch
A HTML crawling program for Livedu(라이브에듀) Academy

## Contents Explained
HTML_FETCH.py is the base python file for creating the HTML_FETCH.exe.
1. When cURL is entered, it is sent to a curl trilling site(https://curlconverter.com/) and the output is saved in the program.
2. The output is then used in request, and from request we extract html and save it via html.parser.
3. From saved html text, we extract needed data(student information and class content information in this case).
4. Extracted data is then sent to the excel file(소견서.xlsx) and is copied as 완성소견서.xlsx.

## Copyrights and License
HTML_FETCH.py DOES NOT have access to Livedu ERP site without user cookies. Therefore, the program itself has no conflict with webpage copyrights or licenses.
