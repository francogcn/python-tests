import requests, csv, datetime
#Playstation 5 price scrapper
#URL corresponds to a recomendations page in ML
url='https://www.mercadolibre.com.ar/recommendations?client=pdp-seller_items-above&limit=20&site_platform=&web_device=desktop&min_recomms=3&bbw_ads=false&include_only_flex=false&site_id=MLA&category_id=MLA438566&item_id=MLA1696108475&product_id=MLA63094449&d2_id=e4366686-d10a-415c-b8aa-2ff616fd5407&use_polycard_order=true&user-zip-code=3300&user-platform=desktop&user-encoded-filters=deal%253AMLA1544201-2&buyer_location=&ads_vpp_tracking_id=bae15642-8a15-4c21-853b-52b1e28dc9dd'
#Request is made via GET Method, using a header
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
req = requests.get(url, headers=HEADERS)

#Response is converted to JSON
data = req.json()

#Gets the product name from the JSON
nombre_producto= data['recommendation_info']['polycards'][1]['components'][0]['title']['text']
#Checks if the product is the requested PS5
if nombre_producto == 'Sony Playstation 5 Consola Slim Standard + Juego Astro Bot Y Gt7 Blanco':
  previous_price = data['recommendation_info']['polycards'][1]['components'][1]['price']['previous_price']['value']
  current_price = data['recommendation_info']['polycards'][1]['components'][1]['price']['current_price']['value']
  print(nombre_producto)
  print('Previous price: AR$', previous_price)
  print('Current price: AR$', current_price)
  #Get current timestamp
  now = datetime.datetime.now()
  now = now.strftime("%Y-%m-%d %H:%M:%S")

  #Save as CSV
  price_list = [now, previous_price, current_price]
  with open('price_list.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(price_list)
    print("CSV saved")


#Shows error message in case is not the right product
else:
  found_url =data['recommendation_info']['polycards'][1]['metadata']['url']
  print("Product not found")
  print(f'Found "{nombre_producto}" instead')
  print(f'URL: {found_url}'
