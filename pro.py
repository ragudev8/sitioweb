# Ejercicio 10
for num in range(1, 1001):
    suma_divisores = 0
    for i in range(1, num):
        if num % i == 0:
            suma_divisores += i
    if suma_divisores == num:
        print(f"{num} es un número perfecto")