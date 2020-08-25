# Decir si un N° ingresado es: negativo, cero o positivo e imprimir mensaje

numeroingresado=float(input("Ingrese un número: "))

if float(numeroingresado)>0:
    print("El número ingresado es positivo")
elif float(numeroingresado)==0:
    print("El número ingresado es igual a cero")
elif float(numeroingresado)<0:
    print("El número ingresado es negativo")
