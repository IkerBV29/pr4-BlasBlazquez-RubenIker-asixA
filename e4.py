"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

e4. Programa que imprimeix un tauler d’escacs per pantalla. Un taulell d’escacs comença amb la casella  Blanca i és de mida 8x8 sempre ;-)
Fer servir:
BLANC = "⬜"
NEGRE = "⬛"
o
NEGRE="██"
BLANC=" "

 Interessant: mostrar els numeris de filera i la lletra de columna (com a la imatge)

Reconocimiento: X > X > X > X

Utilidad: INPUT() > OUTPUT()
"""
#CONSTANTES
NEGRE="██"
BLANC="   "
taula = 8

#Programa
try:
    for i in range(taula): #Repeteix tantes vegades
        taula = taula - 1
        if taula % 2 == 0:
            print(4*str(BLANC+NEGRE))
        else:
            print(4*str(NEGRE+BLANC))
except:
    print("No va")