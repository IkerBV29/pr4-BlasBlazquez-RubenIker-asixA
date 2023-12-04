"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e3. Programa que mostra per pantalla la suma de tots els nombres senars i de tots
els nombres parells inferiors a un número límit, que l’usuari introdueix per teclat.
 Ex: 	ssi el límit é 31 sumaParells 240 i sumaSenars 225
si el límit és 54 sumaParells 702 i sumaSenars 729

Reconocimiento: X > X > X > X

Utilidad: INPUT() > OUTPUT()
"""
sumaP=0
sumaI=0
try:
    limit = int(input())
    LIMITF = limit
    while limit != 0:
        if limit % 2 == 0:
            sumaP = sumaP + limit
            limit = limit - 1
        else:
            sumaI = sumaI + limit
            limit = limit - 1
    print("Si el límit és", LIMITF, "la suma de parells es", sumaP, " i la suma de senars és ", sumaI)

except ValueError:
        print("Datos invalidos")


