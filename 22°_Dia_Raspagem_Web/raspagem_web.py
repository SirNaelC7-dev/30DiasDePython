import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'


resposta = requests.get(url)

status = resposta.status_code
print(status)



url = 'https://archive.ics.uci.edu/ml/datasets.php'

resposta = requests.get(url)
conteudo = resposta.content
soup = BeautifulSoup(conteudo, 'html.parser')
print(soup.title)
print(soup.title.get_text()) 
print(soup.body)
print(resposta.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
table = tables[0] 
for td in table.find('tr').find_all('td'):
    print(td.text)