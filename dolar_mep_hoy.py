import requests, bs4
res = requests.get("https://dolarhoy.com/cotizacion-dolar-bolsa")
res.raise_for_status()
# Parses the content if the request succeeds
soup = bs4.BeautifulSoup(res.text, "html.parser")
mep_dolar = soup.select(".cotizacion_value")
for x in range(len(mep_dolar)):
  print(mep_dolar[x].get_text(separator='\n'))
