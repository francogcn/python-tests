#! python3
import dolarhoy

moneda = int(input("Ingrese el monto en pesos: "))

cotizacion = dolarhoy.get_dolarhoy()

print(f"AR ${moneda} son U$D {moneda*cotizacion}")
