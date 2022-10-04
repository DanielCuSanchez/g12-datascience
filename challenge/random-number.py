# Codigo por @LuisLechuga55 (github)
# Codigo de ejemplo de clase
import random

intentos = 0

name = input("Hola, ¿Como te llamas? ")

numero = random.randint(1, 10)
print("Bien, " + name + " estoy pensando en un numero entre 1 y 10")
print(input("Presiona intro para continuar..."))


while intentos < 3:
  print("Intenta adivinar.")
  respuesta = int(input("Escoge un numero: "))

  intentos = intentos + 1

  if respuesta < numero:
    print("El numero que escogiste es muy bajo.")

  if respuesta > numero:
    print("El numero que escogiste es muy alto.")

  if respuesta == numero:
    print("Felicidades, acertaste el numero")
    break

if respuesta == numero:
  intentos = str(intentos)
  print("Buen trabajo " + name + ", Has adivinado mi numero en " + intentos + " intentos")
  print(input("Presiona intro para salir..."))


if respuesta != numero:
  numero = str(numero)
  print("Fallaste. El numero que estaba pensando era " + numero)
  print(input("Presiona intro para salir..."))
