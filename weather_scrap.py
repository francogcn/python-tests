import requests, bs4
#Download content from weather.com for the cities 'Posadas, Misiones' or 'Wanda, Misiones'

ubi = input("Ingrese la ubicacion: ")
ubi = ubi.lower().strip()
if ubi == "posadas":
  res = requests.get('https://weather.com/es-AR/tiempo/hoy/l/2d06ed300257681d1441a7014c3f72deb9e6073a1a998679ee383c23849ba0e5')
else:
  res = requests.get('https://weather.com/es-AR/tiempo/hoy/l/18e6e7c0ded65486463277de9179836591565039682af2f710c2658222f41895')
#Program halts if download fails
res.raise_for_status()

#Parses the HTML download
soup = bs4.BeautifulSoup(res.text,"html.parser")

#Searches for the element with html class "CurrentConditions--tempValue--zUBSz"
temperature  = soup.select('.CurrentConditions--tempValue--zUBSz')

#Searches for Feels
feels_like = soup.select('.TodayDetailsCard--feelsLikeTempValue--8WgHV')

#If elements are found, prints message with current temperature and what it feels like
if len(temperature) > 0 and len(feels_like) > 0:
  print(f"Temperature in {ubi.capitalize()} is {temperature[0].getText()}C")
  print(f"Feels like: {feels_like[0].getText()}C")
  print("Source: weather.com")
else:
  print("Search failed")
