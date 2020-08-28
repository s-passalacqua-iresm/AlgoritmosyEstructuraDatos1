import funciones

def menu ():
    print(" --------------------------------------MENU--------------------------------------")
    print("1. Número entero mayor a diez")
    print("2. Suma de tres números ")
    print("3. División de cuadrados")
    print("4. Convertir tempratura de Farenheit a Celcius")
    print("----------------------------------------------------------------------------------")

opcioningresada=int(input("Ingrese el número de actividad que quiera realizar: "))

if opcioningresada == 1:
    numenteroingresado = int(input("Ingrese un número entero: "))
    act1=funciones.num_entero_mayor_diez()
    #return print(str(act1))

elif opcioningresada == 2:
    primernum = int(input("Ingrese el primer número entero: "))
    segundonum = int(input("Ingrese el segundo número entero: "))
    tercernum = int(input("Ingrese el tercer número entero: "))

    act2=funciones.suma_tres_numeros(num1=primernum, num2=segundonum, num3=tercernum)
    #return print(str(act2))

elif opcioningresada == 3:
    numentero1 = int(input("Ingrese el primer número entero: "))
    numentero2 = int(input("Ingrese el segundo número entero: "))

    act3=funciones.division_de_cuadrados(num1=numentero1, num2=numentero2)
    #return print(str(act3))

elif opcioningresada == 4:
    act4= funciones.que_temperatura_es_en_celcius()
    #return print(str(f"{act4}°"))

menu()