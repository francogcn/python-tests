#Buscar valor mínimo historico en el csv
import csv
import os

min_price = float('inf') # Initialize with a very high value
min_price_product_info = None

try:
    with open('price_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader, None) # Skip the header row

        if header is None: # Handle empty file case
            print("The CSV file is empty.")
        else:
            # Find the index of 'Current Price'
            try:
                current_price_index = header.index('Current Price')
                product_name_index = header.index('Product Name')
            except ValueError:
                print("CSV header does not contain 'Current Price' or 'Product Name'.")
                exit()

            for row in reader:
                if len(row) > current_price_index:
                    try:
                        # Clean price string (remove non-numeric chars except dot/comma, replace comma with dot)
                        price_str = row[current_price_index].replace('.', '').replace(',', '.')
                        price = float(price_str)
                        if price < min_price:
                            min_price = price
                            min_price_product_info = {
                                "Timestamp": row[header.index('Timestamp')],
                                "Product Name": row[product_name_index],
                                "Previous Price": row[header.index('Previous Price')],
                                "Current Price": price
                            }
                    except ValueError:
                        print(f"Skipping row due to invalid price value: {row[current_price_index]}")

    if min_price_product_info:
        print("\n--- Product with Minimum Current Price ---")
        print(f"Product Name: {min_price_product_info['Product Name']}")
        print(f"Minimum Current Price: AR$ {min_price_product_info['Current Price']:.2f}")
        print(f"Recorded at: {min_price_product_info['Timestamp']}")
        if 'Previous Price' in min_price_product_info:
             print(f"Previous Price (at min recording): AR$ {min_price_product_info['Previous Price']}")
    elif header is not None:
        print("No valid current prices found after header.")

except FileNotFoundError:
    print("The file 'price_list.csv' was not found. Please run the price scraping code first.")
except Exception as e:
    print(f"An error occurred: {e}")#Buscar valor mínimo historico en el csv
import csv
import os

min_price = float('inf') # Initialize with a very high value
min_price_product_info = None

try:
    with open('price_list.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader, None) # Skip the header row

        if header is None: # Handle empty file case
            print("The CSV file is empty.")
        else:
            # Find the index of 'Current Price'
            try:
                current_price_index = header.index('Current Price')
                product_name_index = header.index('Product Name')
            except ValueError:
                print("CSV header does not contain 'Current Price' or 'Product Name'.")
                exit()

            for row in reader:
                if len(row) > current_price_index:
                    try:
                        # Clean price string (remove non-numeric chars except dot/comma, replace comma with dot)
                        price_str = row[current_price_index].replace('.', '').replace(',', '.')
                        price = float(price_str)
                        if price < min_price:
                            min_price = price
                            min_price_product_info = {
                                "Timestamp": row[header.index('Timestamp')],
                                "Product Name": row[product_name_index],
                                "Previous Price": row[header.index('Previous Price')],
                                "Current Price": price
                            }
                    except ValueError:
                        print(f"Skipping row due to invalid price value: {row[current_price_index]}")

    if min_price_product_info:
        print("\n--- Product with Minimum Current Price ---")
        print(f"Product Name: {min_price_product_info['Product Name']}")
        print(f"Minimum Current Price: AR$ {min_price_product_info['Current Price']:.2f}")
        print(f"Recorded at: {min_price_product_info['Timestamp']}")
        if 'Previous Price' in min_price_product_info:
             print(f"Previous Price (at min recording): AR$ {min_price_product_info['Previous Price']}")
    elif header is not None:
        print("No valid current prices found after header.")

except FileNotFoundError:
    print("The file 'price_list.csv' was not found. Please run the price scraping code first.")
except Exception as e:
    print(f"An error occurred: {e}")
