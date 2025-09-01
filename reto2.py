
Num = int(input("Ingrese la cantidad de pacientes: "))


hombres_baja = 0
hombres_normal = 0
hombres_alta = 0
mujeres_baja = 0
mujeres_normal = 0
mujeres_alta = 0


for i in range(1, Num + 1):
    print(f"\nPaciente {i}:")
    hemoglobina = float(input("Ingrese el nivel de hemoglobina: "))
    genero = int(input("Ingrese el genero (1: Masculino, 2: Femenino): "))

    while genero not in (1, 2):
        print("Genero no valido. Intente nuevamente.")
        genero = int(input("Ingrese el genero (1: Masculino, 2: Femenino): "))
    
    if genero == 1:
        if hemoglobina < 12.2:
            print("→ Hombre con alerta: BAJA")
            hombres_baja += 1
        elif hemoglobina > 16.6:
            print("→ Hombre con alerta: ALTA")
            hombres_alta += 1
        else:
            print("→ Hombre con alerta: NORMAL")
            hombres_normal += 1
    
    else:
        if hemoglobina < 12.6:
            print("→ Mujer con alerta: BAJA")
            mujeres_baja += 1
        elif hemoglobina > 15:
            print("→ Mujer con alerta: ALTA")
            mujeres_alta += 1
        else:
            print("→ Mujer con alerta: NORMAL")
            mujeres_normal += 1


print("REPORTE FINAL ")
print(f"Hombres Baja: {hombres_baja}")
print(f"Hombres Normal: {hombres_normal}")
print(f"Hombres Alta: {hombres_alta}")
print(f"Mujeres Baja: {mujeres_baja}")
print(f"Mujeres Normal: {mujeres_normal}")
print(f"Mujeres Alta: {mujeres_alta}")