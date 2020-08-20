#Dado dos número enteros, sabe resultado al dividir cuadrado del
#mayor y cuadrado del menor. Si son =  , escribir un mensaje.

numentero1=int(input("Ingrese el primer número entero: "))
numentero2=int(input("Ingrese el segundo número entero: "))

if int(numentero1)>int(numentero2):
    calculo1=(int(numentero1)**2)/(int(numentero2)**2)
    print(f"El resultado de la operación es: {calculo1}")
else:
    calculo2=(int(numentero2)**2)/(int(numentero1)**2)
    print(f"El resultado de la operación es: {calculo2}")

if str(numentero1)==str(numentero2):
    print(f"Los números ingresados son iguales")