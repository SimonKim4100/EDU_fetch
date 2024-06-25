# EDU_fetch
A HTML crawling program for Livedu(라이브에듀) Academy

## Contents Explained
HTML_FETCH.py is the base python file for creating the HTML_FETCH.exe.
1. Cookies are fetched from webpage using ID and password.
2. The output is then used in request, and from request we extract html and save it via html.parser.
3. From saved html text, we extract needed data(student information and class content information in this case).
4. Extracted data is then sent to the excel file(소견서.xlsx) and is copied as 완성소견서.xlsx.

### Extras
HTML_FETCH.exe uses chromedriver and excel file. Directories are set as the same folder as the exe file. Therefore, if you move/remove chromedriver or the excel file from the folder, you will get errors.

## Copyrights and License
HTML_FETCH.py DOES NOT have access to Livedu ERP database without user cookies. Therefore, the program itself has no conflict with webpage copyrights or licenses.
