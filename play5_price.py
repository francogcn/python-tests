import requests, csv, datetime, os
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
recomendaciones = data['recommendation_info']['polycards']

# Define the CSV file name
csv_file_name = 'price_list.csv'

# Check if the file exists to write headers only once
file_exists = os.path.isfile(csv_file_name)

with open(csv_file_name, 'a', newline='') as file:
  writer = csv.writer(file)
  # Write header only if the file is new
  if not file_exists:
    writer.writerow(['Timestamp', 'Product Name', 'Previous Price', 'Current Price'])

  #Checks if the product is the requested PS5
  for recomendacion in recomendaciones:
    title = recomendacion['components'][0]['title']['text'].lower()
    if 'sony playstation 5' in title or 'consola' in title:
      product_name = recomendacion['components'][0]['title']['text']
      previous_price = recomendacion['components'][1]['price']['previous_price']['value']
      current_price = recomendacion['components'][1]['price']['current_price']['value']
      print(product_name)
      print('Previous price: AR$', previous_price)
      print('Current price: AR$', current_price)
      #Get current timestamp
      now = datetime.datetime.now()
      now = now.strftime("%Y-%m-%d %H:%M:%S")

      #Save as CSV
      price_data = [now, product_name, previous_price, current_price]
      writer.writerow(price_data)
      print(f"Data for '{product_name}' saved to {csv_file_name}")
