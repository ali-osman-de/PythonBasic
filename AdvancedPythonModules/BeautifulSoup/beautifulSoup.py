
html_doc = """

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>First Website</title>
</head>
<body>
<h1 id="header">
Python Course
</h1>
<div class="grup1">
<h2>
Programlama
</h2>
<ul>
<li>Menü 1</li>
<li>Menü 2</li>
<li>Menü 3</li>
</ul>
</div>
<div class="grup2">
<h2>
Modüller
</h2>
<ul>
<li>Menü 1</li>
<li>Menü 2</li>
<li>Menü 3</li>
</ul>
</div>
</body>
</html>
"""

from bs4 import BeautifulSoup

soup =  BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
result = soup.title
result = soup.head
result = soup.body

result = soup.title.string

result = soup.h1
result = soup.h2
result = soup.h2.string
result = soup.h1.string
result = soup.find_all('h2')
result = soup.find_all('h2')[0]
result = soup.find_all('h2')[1]
result = soup.div
result = soup.find_all('div')[1]
result = soup.find_all('div')[1].ul
result = soup.find_all('div')[1].ul.find_all('li')

# for i in result:
#     print(i)

result = soup.div.findChildren()

result = soup.div.findNextSibling()

result = soup.div.findPreviousSibling()



print(result)