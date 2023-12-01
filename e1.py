"""
Ruben Blas Lario, Iker Blazquez Valverde
01/12/2023
M01 UF1 Pr4

Programa que demana a l'usuari la introducció de 10 nombres sencers (que també podrien
ser 10000000 😱😳😈) i ha de mostrar, al final i per pantalla, quants són positius,
quants negatius i quants zero.

Reconocimiento: X > X > X > X

Utilidad: INPUT() > OUTPUT()
"""
    #Contadores p=positivo, n=negativo, zero=0
p=0
n=0
z=0

for _ in range(10):
    try:
        numero=int(input("Ingresa 10 numeros"))

        if numero > 0:
            p = p + 1
        elif numero == 0:
            z = z + 1
        else:
            n = n + 1

    except ValueError:
            print("Dades no valides")
print("Hay ",p,"numeros positivos,",n,"numeros negativos y", z, "zeros")



