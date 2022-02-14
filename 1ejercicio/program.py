# program.py
print ('')
print ('***[Ejecutar un programa]***')
sum = 1 + 2
print(sum)
print ('')
print ('***[La función print()]***')
print('Hola desde la consola')
print ('')
print ('***[Varibales]***')
sum = 1 + 2 # 3
product = sum * 2
print(product)
print ('')
print ('***[Tipos de datos]***')
planetas_en_el_sistema_solar = 8 # int, plutón era considerado un planeta pero ya es muy pequeño
distancia_a_alfa_centauri = 4.367 # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11" #string
print ('')
print ('# Declaramos la variable')
print ('{} = {}'.format('planetas_en_el_sistema_solar',planetas_en_el_sistema_solar))
print ('')
print ('# Descubrimos su tipo de dato')
print (type(planetas_en_el_sistema_solar))
print ('')
print ('# Declaramos la variable')
print ('{} = {}'.format('distancia_a_alfa_centauri',distancia_a_alfa_centauri))
print ('')
print ('# Descubrimos su tipo de dato')
print (type(distancia_a_alfa_centauri))
print ('')
print ('***[Operadores]***')
left_side = 10
right_side = 5
left_side / right_side # 2
print (left_side / right_side)
print ('')
print ('***[Operadores aritméticos]***')
print('Ejemplo 1+1 = {}'.format(1+1))
print ('')
print ('***[Operadores de asignación]***')
print ('')
print('Ejemplo x = 2')
print ('')
print ('***[Fechas]***')
print ('')
# Importamos la biblioteca 
from datetime import date
# Obtenemos la fecha de hoy
date.today()
# Mostramos la fecha en la consola
print(date.today())
print ('')
print ('***[Conversión de tipos de datos]***')
print ('')
print("Today's date is: " + str(date.today()))
print ('')
print ('***[Recopilar información]***')
print ('')
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)
print ('')
print ('***[Trabajar con números]***')
print ('')
print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)
print ('Para que el cálculo funcione correctamente, se le agrego la función int()')
print(int(first_number) + int(second_number))



