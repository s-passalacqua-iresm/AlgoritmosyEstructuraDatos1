#vectores: coleccion de datos

frutas=("manzana", "pera", "banana") # poner corchetes
for fruta in frutas:
    print(fruta)

#Calcular el promedio de los alumnos de un curso que tiene 10 alumnos
acum=0
for i in range (1,11):
    nota=int(input(f"Ingrese nota: {i}: ")
    acum=acum+nota

prom=acum/10
print(f"El promedio general del curso es: {prom}")



