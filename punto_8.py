def NumerosPrimos(n):
    while n <= 100:
        i = 2
        primo = True
        while i < n:
            if n % i == 0:
                primo = False
                break
            i += 1
        if primo:
            print(n)
        n += 1

if __name__ == "__main__":
    n = 2
    NumerosPrimos(n)