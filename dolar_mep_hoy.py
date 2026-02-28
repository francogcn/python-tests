#Import required libraries
import requests, bs4

#Send HTML request to dolarhoy.com
res = requests.get("https://dolarhoy.com/cotizacion-dolar-bolsa")

#Program halts if download is fails
res.raise_for_status()

# Parses the content if the request succeeds
soup = bs4.BeautifulSoup(res.text, "html.parser")

#Selects html elment with class .cotizacion_value
mep_dolar = soup.select(".cotizacion_value")

#Prints the current value for mep dolar
for x in range(len(mep_dolar)):
  print(mep_dolar[x].get_text(separator='\n'))
