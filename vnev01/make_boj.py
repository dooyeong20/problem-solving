import requests
from bs4 import BeautifulSoup
import os.path


no = input('no : ')
ranks =['bronze', 'silver', 'gold']
rank = ranks[int(input('silver - 1, Gold - 2 : '))]

webpage = requests.get("https://www.acmicpc.net/problem/" + no)
soup = BeautifulSoup(webpage.content, "html.parser")
problem_title = soup.select("#problem_title")[0].get_text().replace(' ', '')

content = 'from sys import stdin'
path = '../problems/' + rank + '/'
file_name = path + problem_title + '.py'
file_name.replace(' ', '')

if os.path.isfile(file_name):
    print('file already exists')
else:
    f = open(file_name, "w")
    f.write(content)
    f.close()
    print('file created !')