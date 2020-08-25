#Algotimo que lea entero y verifique sea mayor a 10. 
#Si lo es, escribir el número, si no, mensaje que diga que es menor o igual

numeroentero=int(input("Ingrese un número entero: "))

if int(numeroentero) >10:
    print(f"{numeroentero}")
else:
    print(f"El número ingresado es menor o igual a 10")