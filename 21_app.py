def calcular_monto_total ():
    monto_sin_igv = float(input("Ingrese el monto sin IGV: "))
    tasa_igv = float(input("Ingrese la tasa del IGV (en %): "))
    igv = monto_sin_igv * (tasa_igv / 100)
    monto_total = monto_sin_igv + igv

    print(f"Monto sin IGV: S/ {monto_sin_igv:.2f}")
    print(f"IGV ({tasa_igv}%): S/ {igv:.2f}")
    print(f"Monto total: S/ {monto_total:.2f}")

calcular_monto_total()