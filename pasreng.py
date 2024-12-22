#PARSING
import requests

url = "https://coinmarketcap.com/"
response = requests.get(url)

if response.status_code == 200:
    print("Успешное подключение к сайту")

else:
    print("AN EROR OCURED SIR", response.status_code)

print(response.text[:500]) #Ограничение вывода первым 500 символамм

from bs4 import BeautifulSoup
html = response.text

soup = BeautifulSoup(html, 'html.parser')

title_tag = soup.find("title")
print(title_tag)
#or
print(title_tag.text)

rows = soup.find_all("tr")

print(rows)
for row in rows[1: 11]: #первый tr на сайте это заголовки таблицы, так что начинаем с первого, он нам не нужен
    name_tag = row.find("p", class_="sc-65e7f566-0 byYAWx coin-item-symbol") #класс берётся с сайта саморучно
    price_tag = row.find("div", class_="sc-b3fc6b7-0 dzgUIj")#потому что в отличии от верха, он находится не в таблице а в div-e c определенным классом
    number_tag = row.find("p", class_="sc-71024e3e-0 jBOvmG")
    h1_tag = row.find("div", class_="sc-b3fc6b7-0 dzgUIj").text
    h24_tag = row.find("span", class_="sc-a59753b0-0 ivvJzO").text
    d7_tag = row.find("span", class_="sc-a59753b0-0 ivvJzO").text
    marketCap_tag = row.find("span", class_="sc-11478e5d-1 jfwGHx").text
    print(f"Number: {number_tag.text} | crypto: {name_tag.text} | price: {price_tag.text} | 1h%: {h1_tag} | 24h%: {h24_tag} | 7d%: {d7_tag} | Market Cap: {marketCap_tag}")
