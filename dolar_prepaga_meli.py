import requests, bs4

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
res = requests.get("https://www.mercadopago.com.ar/cards/commons/dollar-exchange", headers=headers)
res.raise_for_status()
# Parses the content if the request succeeds
soup = bs4.BeautifulSoup(res.text, "html.parser")
dolar_prepaga = soup.select('.andes-money-amount')
for dolar in dolar_prepaga:
  print(dolar.getText())
