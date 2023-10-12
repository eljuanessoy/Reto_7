n = int(input("Ingrese un número natural mayor o igual a 2: "))
print(f"Los números pares anteriores a {n} en forma descendente es: ")

while n > 2:
    if n % 2 == 0:
        n -= 2
    else:
        n = n + 1
        n -= 2
    print(n)