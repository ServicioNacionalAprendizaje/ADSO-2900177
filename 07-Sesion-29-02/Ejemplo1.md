Análisis
- Productos `arroz: $2.900`, `frijol: $3.200`, `cereal: $12:800`
- Descuento `arroz: 3%`, `frijol: 9%`, `cereal: 2%`
- El usuario debe indicar cuanto lleva de cada producto
- Mostrar el valor sin descuento de cada producto
- Mostrar el varor total sin descuento de los productos
- Mostrar el varor total con descuento de los productos 

 ```json
    arroz: a, 
    frijol: f,
    cereal: c,
    precioUnitarioArroz: pua,
    precioUnitarioFrijo: puf,
    precioUnitarioCereal: puc,
    precioArroz: pa,
    precioFrijol: pf,
    precioCereal: pc,
    precioTotalConDescuento: pt,
    precioTotalSinDescuento: ptsd
 ```


```
    INICIO 
        //Definir las variables
        DEFINIR COMO pua, puf, puc, pa, pf, pc, pt, ptsd REAL
        DEFINIR COMO a,  f, c ENTERO

        //Inicializar varaibles
        pua = 2900
        puf = 3200
        puc = 12800
        pa = 0
        pf = 0
        pc = 0
        pt = 0
        ptsd = 0
        a = 0
        f = 0
        c = 0

        //Capturar datos 
        ESCRIBIR "Digite la cantidad de arroz a llevar: "
        LEER a

        ESCRIBIR "Digite la cantidad de frijo a llevar: "
        LEER f

        ESCRIBIR "Digite la cantidad de cereal a llevar: "
        LEER c

        //Proceso
        pa = pua * a
        pf = puf * f
        pc = puc * c
        
        ptsd =  pa + pf + pc
        pt = ptsd - ( (pa*0.03) + (pf * 0.09) + (pc* 0.02))
        

        //Salida
        ESCRIBA "El valor a pagar por arroz: ",pa
        ESCRIBA "El valor a pagar por frijol: ",pf
        ESCRIBA "El valor a pagar por cereal: ",pc

        ESCRIBA "El valor a pagar sin descuento: ",ptsd
        ESCRIBA "El valor a pagar con descuento: ",pt

    FIN
```