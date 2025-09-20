
import bs4 #importa a biblioteca beautifulsoap 4
import requests #importar a biblioteca request

url = "https://quotes.toscrape.com/" #grava o site quotes
quotes = requests.get(url) #importa o código do site
soup = bs4.BeautifulSoup(quotes.text, 'html.parser') #converte o quote em html

frase = soup.find_all('div' , class_='quote') #encontrou todas as div

for div in frase:
    texto = div.find('span', class_='text')
    print(texto)