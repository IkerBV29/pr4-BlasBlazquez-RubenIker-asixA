"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e5. Programa que realitza la multiplicació, de dos nombres sencers,  mitjançant sumes

Reconocimiento: X > X > X > X

Utilidad: INPUT() > OUTPUT()
"""
try:
    numeros = input()
    numeros = numeros.split(" ")
    n1 = int(numeros[0])
    n2 = int(numeros[1])
    multiplicacio = 0
    for i in range(n2):
        multiplicacio = multiplicacio + n1
    print(multiplicacio)
except ValueError:
    print("Dades no válides")

