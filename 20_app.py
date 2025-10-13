# Calcular el monto incluido el IGV

monto_con_igv = float(input("Ingrese el monto con IGV incluido: "))
monto_sin_igv = monto_con_igv / 1.18
igv = monto_con_igv - monto_sin_igv

print("Monto sin IGV: S/", round(monto_sin_igv, 2))
print("IGV (18%): S/", round(igv, 2))