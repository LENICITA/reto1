hemoglobina = float(input("ingrese el valor de homoflobina: "))
genero = int(input("ingrese el el genero (1 = masculino , 2 = femenino): "))

if genero == 1:
    if hemoglobina < 12.2:
        print("Baja")
    elif hemoglobina <= 16.6:
        print("Normal")
    else:
        print("Alta")
elif genero == 2:
    if hemoglobina < 12.6:
        print("Baja")
    elif hemoglobina <= 15:
        print("Normal")
    else:
        print("Alta")
else:
    print("No es posible generar la alerta")