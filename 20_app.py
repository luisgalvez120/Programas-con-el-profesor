# Calcular el monto incluido el IGV

monto_total = float(input("Ingrese el monto total: "))

monto_sin_igv = monto_total * (82 / 100)
igv = monto_total * (18 / 100)

print("Monto sin IGV: S/", round(monto_sin_igv, 2))
print("IGV: S/", round(igv, 2))