import funciones

celcius=funciones.que_temperatura_es_en_celcius(32)  #función agarra 30, lo lleva a principal, hace el cálculo y vuelve el resultado acá
print(f"La temperatura en celcius es:   {celcius}")

temp=funciones.que_temperatura_es()
print(f"La temperatura es: {temp}")

resultado=funciones.division_de_cuadrados(2, 4)
print(f"La division de los cuadrados es: "{resultado}")

res_100=funciones.division_de_cuadrados_x_100(2, 4)  # resultado x 100
print(f"La división de los cuadrados multiplicados por 100 es: {res_100}")

menu()