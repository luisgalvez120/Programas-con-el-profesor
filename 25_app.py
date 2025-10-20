# Funcion para calcular monto pago

def calcularMonto(precio, descuento):
    montoDescuento = precio * (descuento/100)
    montoPago = precio - montoDescuento
    return montoPago

# Utilizando la funcion
precio = 5000
desceunto = 10

montoPago = calcularMonto(precio, descuento)
print(f"El precio del producto es: S/. {precio}")
print(f"El porcentaje de descuento es: S/. {descuento}")
print(f"El monto a pagar es: S/. {montoPago:.2f}")