import requests, bs4
res = requests.get('https://weather.com/es-AR/tiempo/hoy/l/2d06ed300257681d1441a7014c3f72deb9e6073a1a998679ee383c23849ba0e5')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text,"html.parser")
temperature  = soup.select('.CurrentConditions--tempValue--zUBSz')
if len(temperature) > 0:
  print(f"Temperature in Posadas is {temperature[0].getText()}C")
  print("Source: Weather.com")
