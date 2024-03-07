num = 0.0
bandera = True
while bandera == True:
    try:
        num = float(input("Introduce un número: "))
        if num % 2 == 0:
            print("El número es par")
        else:
            print("El número es impar")
        bandera = False
    except:
        print("no es un numero señor usuario, por favor ingrese un numero valido")
        num = 0