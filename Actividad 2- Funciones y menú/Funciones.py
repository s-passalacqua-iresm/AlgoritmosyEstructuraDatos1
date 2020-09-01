#1: método sin retorno ni parámetros: chequear si num entero > 10
def num_entero_mayor_diez(numIngresado): # La funcion debia ser sin parametros, por lo que el numero deberia ingresarse directamente en la funcion
    if (numIngresado > 10):
        print(f"{numIngresado}")
    else:
        print(f"El número ingresado es menor o igual a 10")

#2: método sin retorno y con parámetros: recibir 3 números....
def suma_tres_numeros(primernum=0, segundonum=0, tercernum=0):

     suma = primernum + segundonum

     if(suma == tercernum):
         print("La suma de los dos primeros números enteros es igual al tercero ingresado")
     else:
         print("La suma de los dos primeros números enteros no es igual al tercero ingresado")

#3: método con retorno y parámetros con 2 números enteros
def division_de_cuadrados(numEntero1 , numEntero2 ):

    if (numEntero1 > numEntero2):
        calculo1 = (numEntero1*2) / (numEntero2*2)
        return str(f"El resultado de la operación es: {calculo1}") # Solo debe retornar calculo1: return calculo 1
    elif(numEntero2 >  numEntero1):
        calculo2 = (numEntero2*2 ) / (numEntero1*2)
        return str(f"El resultado de la operación es: {calculo2}") # Solo debe retornar calculo2: return calculo 2
    else:
        return str(f"Los números ingresados son iguales;") # Solo debe retornar 1: return 1

#4: método con retorno y sin parámetros: convertir temperaturas de F a C
def que_temperatura_es_en_celcius():
    farenheit=int(input("Ingrese la temperatura en Farenheit: "))
    celcius = int(5/9 * (farenheit - 32))
    return str(f"La temperatura en celcius es de: {celcius}°") # Solo debe retornar celcius: return celcius
