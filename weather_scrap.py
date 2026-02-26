#Import main modules
import requests, bs4
#Download content from weather.com for city 'Posadas, Misiones'
res = requests.get('https://weather.com/es-AR/tiempo/hoy/l/2d06ed300257681d1441a7014c3f72deb9e6073a1a998679ee383c23849ba0e5')
#Program halts if download fails
res.raise_for_status()
#Parses the HTML download
soup = bs4.BeautifulSoup(res.text,"html.parser")
#Searches for the element with html class "CurrentConditions--tempValue--zUBSz"
temperature  = soup.select('.CurrentConditions--tempValue--zUBSz')
#If element is found, prints message with current temperature
if len(temperature) > 0:
  print(f"Temperature in Posadas is {temperature[0].getText()}C")
  print("Source: Weather.com")
