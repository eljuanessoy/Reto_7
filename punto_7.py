n = int(input("Ingresa un valor de 2 a 50: "))
x : int = n
print(f"Los divisores de {n} son:")

while x >= 1:
    if n % x == 0:
        print(x)
    x -= 1