#! python3

#Importacion de modulos
from dolarhoy import DolarHoy

#Instancio la clase DolarHoy
dolar_hoy = DolarHoy()

#El valor de la cotizacion se obtiene mediante un fetch del modulo dolarhoy
cotizacion = dolar_hoy.get_oficial_price()

#Se pide al usuario ingresar el monto a convertir
moneda = int(input("Ingrese el monto en pesos: "))

#Se imprime el monto convertido
print(f"AR ${moneda} son U$D {moneda*cotizacion['venta']}")
