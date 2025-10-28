# Solicitar al usuario 5 nombres de paises

paises = []
for i in range(5):
    pais = input(f"Ingrese el nombre del pais {i+1} :")
    paises.append(pais)

# Imprimir los elementos de la lista
print("\nPaises ingresados:")
for pais in paises:
    print(pais)