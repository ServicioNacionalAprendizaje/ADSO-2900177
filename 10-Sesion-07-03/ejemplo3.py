
while True: 
    try: 
        numUno = float(input("Digite el primer numero: "))
        numDos = float(input("Digite el segundo numero:"))

        if numDos < 0 and numUno % 2 != 0:
            if numUno > numDos:
                print(numUno,",",numDos)
            else: 
                print(numDos,",",numUno)
            break
        else: 
            if(numUno > numDos): 
                print(numDos,",",numUno)
            else: 
                print(numUno,",",numDos)
            break
    except:
        print("Error, valor invalido")