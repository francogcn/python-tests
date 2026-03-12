#product price monitoring with python

#Import required modules
import requests
from bs4 import BeautifulSoup
import time
import csv
import os

# --- Configuración ---
# URL del producto a monitorear (ejemplo, puedes cambiarlo)
link_play="https://www.mercadolibre.com.ar/sony-playstation-5-consola-slim-digital-juego-astro-bot-y-gt7/p/MLA63094449?pdp_filters=deal%3AMLA1544201-2#polycard_client=splinter&c_element_order=3&deal_print_id=9ca10cd0-1e60-11f1-b699-4ba5a30df6bf&L=llena-tu-carrito-de-cyber-ofertas&type=product&c_tracking_id=9ca10cd0-1e60-11f1-b699-4ba5a30df6bf&c_uid=97ebbf1c-bb44-3208-bd17-f69ec3e97c66&V=3&c_campaign=llena-tu-carrito-de-cyber-ofertas&c_id=%2Fsplinter%2Fcarouseldynamicitem&position=3&c_label=%2Fsplinter%2Fcarouseldynamicitem&c_container_id=MLA1544201-1&c_global_position=25&c_element_id=97ebbf1c-bb44-3208-bd17-f69ec3e97c66&wid=MLA2746671250&sid=splinter"
PRODUCT_URL = link_play # Reemplaza con la URL real de un producto
PRODUCT_NAME = "Play 5" # Nombre para identificar el producto
CSV_FILE = "price_history.csv" # Archivo para guardar el historial de precios
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def get_product_price(url, headers):
    """
    Extrae el precio de un producto de la URL dada.
    Necesitarás ajustar los selectores CSS según la estructura del sitio web.
    """
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Lanza una excepción para errores HTTP

        soup = BeautifulSoup(response.text, 'html.parser')
