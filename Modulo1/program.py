# program.py
from datetime import date
summ = 1 + 2
print(summ)

print('')

print('Hola desde la consola.')

print('')

sum = 1 + 2  # 3
product = sum * 2
print(product)

print('')

# int, plutón era considerado un planeta pero ya es muy pequeño
planetas_en_el_sistema_solar = 8
distancia_a_alfa_centauri = 4.367  # float, años luz
puede_despegar = True
transbordador_que_aterrizo_en_la_luna = "Apollo 11"  # string
tipo = type(distancia_a_alfa_centauri)
print(tipo)

print('')

left_side = 10
right_side = 5
print(left_side / right_side)  # 2

print('')

print(date.today())
print("Today's date is: " + str(date.today()))

print('')

print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print('')

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(first_number + second_number)

print(int(first_number) + int(second_number))