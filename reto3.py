
N = int(input())

suma_hombres = 0
suma_mujeres = 0
cont_hombres = 0
cont_mujeres = 0
lista_hombres = []
lista_mujeres = []

# Lectura de pacientes
for _ in range(N):
    valores = input().split()
    hemoglobina = float(valores[0])
    genero = int(valores[1])

    while genero != 1 and genero != 2:
        valores = input().split()
        hemoglobina = float(valores[0])
        genero = int(valores[1])

    if genero == 1: # Masculino
        suma_hombres += hemoglobina
        cont_hombres += 1
        lista_hombres.append(hemoglobina)
    else: # Femenino
        suma_mujeres += hemoglobina
        cont_mujeres += 1
        lista_mujeres.append(hemoglobina)

# Calcular promedios
prom_hombres = suma_hombres / cont_hombres if cont_hombres > 0 else 0.00
prom_mujeres = suma_mujeres / cont_mujeres if cont_mujeres > 0 else 0.00

# Determinar alertas
if prom_hombres < 12.2 and cont_hombres > 0:
    alerta_hombres = "Baja"
elif prom_hombres > 16.6:
    alerta_hombres = "Alta"
else:
    alerta_hombres = "Normal"

if prom_mujeres < 12.6 and cont_mujeres > 0:
    alerta_mujeres = "Baja"
elif prom_mujeres > 15:
    alerta_mujeres = "Alta"
else:
    alerta_mujeres = "Normal"

# Comparaciones con el promedio
hombres_mayor = hombres_menor = hombres_igual = 0
for h in lista_hombres:
    if h > prom_hombres:
        hombres_mayor += 1
    elif h < prom_hombres:
        hombres_menor += 1
    else:
        hombres_igual += 1

mujeres_mayor = mujeres_menor = mujeres_igual = 0
for m in lista_mujeres:
    if m > prom_mujeres:
        mujeres_mayor += 1
    elif m < prom_mujeres:
        mujeres_menor += 1
    else:
        mujeres_igual += 1

# Imprimir resultados
print(f"{prom_hombres:.2f} {alerta_hombres}")
print(f"{prom_mujeres:.2f} {alerta_mujeres}")
print(hombres_mayor, mujeres_mayor)
print(hombres_menor, mujeres_menor)
print(hombres_igual, mujeres_igual)