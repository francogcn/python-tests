#Import required modules
import requests, bs4
#Declare headers to access page as user
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
#Send HTTP request
res = requests.get("https://www.mercadopago.com.ar/cards/commons/dollar-exchange", headers=headers)
#Program halts if doonload fails
res.raise_for_status()
# Parses the content if the request succeeds
soup = bs4.BeautifulSoup(res.text, "html.parser")
debit_dolar = soup.select('.andes-money-amount')
#Prints the results for MEP Dolar
for dolar in debit_dolar:
  print(dolar.getText())
