import funciones

def menu ():

    print(" --------------------------------------MENU--------------------------------------")
    print("1. Número entero mayor a diez")
    print("2. Suma de tres números ")
    print("3. División de cuadrados")
    print("4. Convertir temperatura de Farenheit a Celcius")
    print("----------------------------------------------------------------------------------")
    opIngresada = int(input("Ingrese la opción que desea realizar: "))

    if(opIngresada == 1):
        numIngresado = int(input("Ingrese un número entero: "))
        funciones.num_entero_mayor_diez(numIngresado) # La funcion no debe recibir parametros el numero debe pedirse directamente en la funcion

    elif(opIngresada == 2):
        primernum = int(input("Ingrese el primer número entero: "))
        segundonum = int(input("Ingrese el segundo número entero: "))
        tercernum = int(input("Ingrese el tercer número entero: "))
        funciones.suma_tres_numeros(primernum, segundonum, tercernum) # OK

    elif(opIngresada == 3):
        num1 = int(input("Ingrese el primer número entero: "))
        num2 = int(input("Ingrese el segundo número entero: "))
        act3 = funciones.division_de_cuadrados(num1, num2)
        return print(act3) # Esta linea deberia ser: print(f"El resultado de la operación es: {act3}"), sin usar la palabra reservada return

    elif (opIngresada == 4):
        act4 = funciones.que_temperatura_es_en_celcius()
        return print(act4) # Esta linea deberia ser: print(f"La temperatura en celcius es de: {act4}°"), sin usar la palabra reservada return

menu()

