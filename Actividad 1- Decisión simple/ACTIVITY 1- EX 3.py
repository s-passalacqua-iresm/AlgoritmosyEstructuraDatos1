#Convertir temperaturas de Fahrenheit a Celcius
#Fórmula: C°= (5/9). (°F -32)

tempingresada=float(input("Ingrese la temperatura en grados Farenheit: "))

calculoconversion=5/9*(float(tempingresada)-32)

print(f"La temperatura que usted ingresó en grados C° es igual a {calculoconversion}")