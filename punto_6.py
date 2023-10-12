import random
def adivinar():
    print("Piensa en un número de 1 a 100, de seguro lo adivinare a la primera :D")
    print("(Escribe 'Si' si es igual, 'Menor' si es menor o 'Mayor' si es mayor)")
    min = 1
    max = 100
    while True: 
        n = random.randint(min, max)
        print(f"¿El número en el que pensaste es {n}?")
        respuesta = input()
        if respuesta == 'Si':
            print("Ves? Te dije que lo adivinaria a la primera")
            break
        elif respuesta == 'Menor':
            max = n - 1
        elif respuesta == 'Mayor':
            min = n + 1
        else:
            print("Creo que deberias leer las instrucciones que te di :d")
            break
adivinar()