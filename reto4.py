def clasificar_materia(valor):
    if valor > 5:
        return 3 
    elif valor > 4:
        return 2 
    elif valor >= 3:
        return 1 
    else:
        return 0 

def clasificar_p2o5(valor):
    if valor > 69:
        return 3
    elif valor >= 57:
        return 2
    elif valor >= 46:
        return 1
    else:
        return 0

categorias = ["no apto", "marginalmente apto", "moderadamente apto", "sumamente apto"]

datos = list(map(float, __import__("sys").stdin.read().split()))

n = int(datos[0])
datos = datos[1:]

materia = []
p2o5 = []
pos = 0

for _ in range(n):
    fila = datos[pos:pos+7]
    materia.append(fila)
    pos += 7

for _ in range(n):
    fila = datos[pos:pos+7]
    p2o5.append(fila)
    pos += 7

conteo_global = [0, 0, 0, 0]

mayores = []
menores = []

for i in range(n):
    conteo_zona = [0, 0, 0, 0]
    for j in range(7):
        cat_materia = clasificar_materia(materia[i][j])
        cat_p2o5 = clasificar_p2o5(p2o5[i][j])
        categoria = min(cat_materia, cat_p2o5)
        conteo_global[categoria] += 1
        conteo_zona[categoria] += 1

    max_freq = max(conteo_zona)
    mejores_candidatos = [idx for idx, val in enumerate(conteo_zona) if val == max_freq]
    mejor_cat = categorias[max(mejores_candidatos)]
    mayores.append(mejor_cat)

    min_freq = min(conteo_zona)
    peores_candidatos = [idx for idx, val in enumerate(conteo_zona) if val == min_freq]
    peor_cat = categorias[max(peores_candidatos)]
    menores.append(peor_cat)

print(*conteo_global)
print(",".join(mayores))
print(",".join(menores))