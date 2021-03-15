import requests

from bs4 import BeautifulSoup


url = 'http://cbr.ru/scripts/XML_daily.asp'

document = requests.get(url)

soup = BeautifulSoup(document.content, "lxml-xml")
valute = soup.find('Valute', ID="R01200")

print(valute.find('Nominal').text, valute.find('Name').text,
      'равно', valute.find('Value').text, 'рублей')
