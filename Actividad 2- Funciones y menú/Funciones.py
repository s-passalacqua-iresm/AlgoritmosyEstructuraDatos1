#1: método sin retorno ni parámetros: chequear si num entero > 10

def num_entero_mayor_diez(numenteroingresado):
    if int(numeroentero) > 10:
        print(f"{numeroentero}")
    else:
        print(f"El número ingresado es menor o igual a 10")

#2: método sin retorno y con parámetros: recibir 3 números....

def suma_tres_numeros(primernum=0, segundonum=0, tercernum=0):

    if int(primernum) + int(segundonum) == int(tercernum):
        print("La suma de los dos primeros números enteros es igual al tercero ingresado")
    else:
        print("La suma de los dos primeros números enteros no es igual al tercero ingresado")

#3: método con retorno y parámetros con 2 números enteros

def division_de_cuadrados(numentero1=1, numentero2=1):

    if int(numentero1)>int(numentero2):
        calculo1=(int(numentero1)**2)/(int(numentero2)**2)
        return(str((f"El resultado de la operación es: {calculo1}")))

    elif int(numentero2)>int(numentero1):
        calculo2=(int(numentero2)**2)/(int(numentero1)**2)
        return(str(print(f"El resultado de la operación es: {calculo2}")))

    else:
        return(str(print(f"Los números ingresados son iguales")))


#4: método con retorno y sin parámetros: convertir temperaturas de F a C

def que_temperatura_es_en_celcius():
    farenheit=int(input("Ingrese la temperatura en Farenheit: "))
    celcius = int(5/9 * (farenheit - 32))
    return celcius
