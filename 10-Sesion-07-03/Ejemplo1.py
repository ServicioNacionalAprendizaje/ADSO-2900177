import math

x = 0
while x == 0:
    try:
        x = float(input("Introduce un número: "))
        if x>5:
            print("El valor de x es mayor que 5")
        else: 
            print("El valor de x es menor o igual que 5")
    except:
        print("El valor introducido no es un número")
        x = 0

