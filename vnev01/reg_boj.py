import requests
from bs4 import BeautifulSoup
import os.path

title = ''
badge = ''
no = input('번호 : ')
url = "https://solved.ac/search?query=" + no
problem_url = "https://www.acmicpc.net/problem/" + no
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, "html.parser")

nos = soup.select(
    'div.sticky-table-cell > span > .ProblemInline__ProblemStyle-cvf1lm-0 > span')
badges = soup.select(
    'div.sticky-table-cell > span > .ProblemInline__ProblemStyle-cvf1lm-0 > img')
titles = soup.select('div.sticky-table-cell > span > a.hover_underline')

for i in range(len(nos)):
    if nos[i].get_text() == str(no):
        title = titles[i].get_text()
        rank = badges[i]['alt']
        badge = badges[i]['src']
        break

print(f'[{rank}] {no} - {title}')
content = '<img height="25px" width="25px=" src="' + \
    badge + '"/> [' + title + '](' + problem_url + ')'

file_path = 'README.md'

f = open(file_path, "a", encoding='utf8')
f.write('\n')
f.write(content)
f.close()
print('Done !')
