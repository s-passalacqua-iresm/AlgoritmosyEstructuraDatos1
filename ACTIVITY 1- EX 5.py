# Ingresar 3 números enteros y determinar:
# si la suma del primero y el segundo es igual al tercero
# Si se cumple: la suma es igual al tercero, si no, la suma es distinta

primernum=int(input("Ingrese el primer número entero: "))
segundonum=int(input("Ingrese el segundo número entero: "))
tercernum=int(input("Ingrese el tercer número entero: "))

if int(primernum)+int(segundonum)==int(tercernum):
    print("La suma de los dos primeros números enteros es igual al tercero ingresado")
else:
    print("La suma de los dos primeros números enteros no es igual al tercero ingresado")