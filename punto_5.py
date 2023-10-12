m = int(input("Ingrese un número natural: "))
ResultadoFactorial = 1

while m > 0:
  ResultadoFactorial *= m
  m -= 1

print(f"El factorial del valor ingresado es: {ResultadoFactorial}")