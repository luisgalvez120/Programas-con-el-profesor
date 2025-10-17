# Ejercicio 2 - Funciones

# Convertir de soles a dolares
def convertirMoneda(montoSoles, tipoCambio):
    montoDolares = montoSoles / tipoCambio
    return montoDolares

# Utilizando la Funcion
compraDolares = convertirMoneda(2000, 3.48)
print(f"El monto en dolares es: $ {compraDolares: .2f} dolares")