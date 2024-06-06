Leer un entero e imprimir si el números par o impar y si es positivo o no.

```
INICIO
    Definir num Como Real
    num = 0.0
    Mientras num = 0.0
        Escribir "Digite un numero"
        Leer num
        Si EsNumero(num) Entonces:
            Si num % 2 = 0 entonces:
                Escribir "El número digitado es par"
                Si num < 0
                    Escribir "El número digitado es negativo"
                Sino
                    Escribir "El número digitado es positivo"
                Finsi
            Sino
                Escribir "El numero digitado es impar"
                Si num < 0
                    Escribir "El número digitado es negativo"
                Sino
                    Escribir "El número digitado es positivo"
                Finsi
            Finsi
        Sino
            num = 0.0
            Escribir "Error: Digitó un caracter, por favor ingrse un número"
            Escribir "Por favor intentelo de nuevo"
        Finsi
FIN
```

```py
num = 0.0
bandera = True
while bandera == True:
    try:
        num = float(input("Introduce un número: "))
        if num % 2 == 0:
            print("El número es par")
            if num < 0:
                print("El número es negativo")
            else:
                print("El número es negativo")
        else:
            print("El número es impar")
            if num < 0:
                print("El número es negativo")
            else:
                print("El número es negativo")
        bandera = False
    except:
        print("no es un numero señor usuario, por favor ingrese un numero valido")
        num = 0
```