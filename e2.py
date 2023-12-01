"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e2. Programa que mostra un triangle amb nombres a les cantonades.  Cal demanar quina alçada ha de tenir el triangle. Els valors permesos per a l'alçada son entre 2 i 9. (ambdós inclosos)
INPUT
Alçada del triangle: 5
OUTPUT
1
2 2
3   3
4     4
5 5 5 5 5

Reconocimiento:  Alçada del triangle > secuencia del 1 al 5 > separacio entre cantonades > base del triangle

Utilidad: INPUT(Alçada del triangle) > OUTPUT(un conjunt de strings que formen un triangle amb nombres desde el 1 fins la alçada a les cantonades)
"""
"""
"""
#INPUT(Alçada del triangle)
Altura = int(input())

#secuencia del 1 al 5
for i in range(int(Altura)+1):print(i)