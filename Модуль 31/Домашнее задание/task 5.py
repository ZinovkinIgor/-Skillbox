"""
Задача 5. Web scraping
Что нужно сделать
Дан несложный пример HTML-страницы: Sample Web Page.

Изучите код этой страницы и реализуйте программу, которая получает список всех подзаголовков сайта (они заключены в теги <h3>).

Ожидаемый результат:

['CONTENTS', '1. Creating a Web Page', '2. HTML Syntax', '3. Special Characters',
'4. Converting Plain Text to HTML', '5. Effects', '6. Lists', '7. Links', '8. Tables',
'9. Viewing Your Web Page', '10. Installing Your Web Page on the Internet',
'11. Where to go from here', '12. Postscript: Cell Phones']



Сделайте так, чтобы программа работала для любого сайта, где есть такие теги.

"""
import requests
import re

sites = requests.get('http://www.columbia.edu/~fdc/sample.html')
text = sites.text
# print(text)
list_headings = []

for headings in text.split('\n'):
    if re.findall(r'<[h,3]{2}', headings):
        headings_start = re.search(r'>', headings)
        headings_stop = re.search(r'</h3>', headings)
        start, stop = headings_start.span(), headings_stop.span()
        list_headings.append(headings[start[1]: stop[0]])
    else:
        pass

print(list_headings)
