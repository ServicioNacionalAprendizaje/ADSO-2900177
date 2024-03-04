Condicionales - `simple` y `anidado`

```
    SI () ENTONCES
        SI () ENTONCES
            SI () ENTONCES
                SI () ENTONCES
                    SI () ENTONCES

                    SINO 

                    FIN SI
                SINO 

                FIN SI
            SINO 

            FIN SI
        SINO 

        FIN SI
    SINO 

    FIN SI
```

```java
    if(){
        if(){
            if(){
                if(){
                    if(){

                    }else{
                        
                    }
                }else{
                    
                }
            }else{
                
            }
        }else{
            
        }
    }else{

    }
```

```python
    if x > 2:
    
    else:
        if x > 2:
        
        else:
            if x > 2:
        
            else:
                if x > 2:
                
                else:
    

```

1. `Ejemplo:`


* Inversión de la persona 1: p1
* Inversión de la persona 2: p2
* Inversión de la persona 3: p3
* Inversión total: it
* Porcentaje de la inversión de la persona 1: pp1
* Porcentaje de la inversión de la persona 2: pp2
* Porcentaje de la inversión de la persona 3: pp3

```
    INICIO 
        //Declarar variables
        p1 = 0;
        p2 = 0;
        p3 = 0;
        it = 0;
        pp1 = 0;
        pp2 = 0;
        pp3 = 0;

        //Capturar datos
        ESCRIBA "Por favor, digite le valor de la inversión de la persona 1: "
        LEER p1
        ESCRIBA "Por favor, digite le valor de la inversión de la persona 2: "
        LEER p2
        ESCRIBA "Por favor, digite le valor de la inversión de la persona 3: "
        LEER p3

        //Procesar datos
        it = p1 + p2 + p3

        pp1 = (p1/it)*100
        pp2 = (p2/it)*100
        pp3 = (p3/it)*100

        //Salida 
        ESCRIBA "El procentaje que le correspondio a la persona 1 por la inversión de $",p1," es de: ",pp1,"%."
        ESCRIBA "El procentaje que le correspondio a la persona 2 por la inversión de $",p2," es de: ",pp2,"%."
        ESCRIBA "El procentaje que le correspondio a la persona 3 por la inversión de $",p3," es de: ",pp3,"%."

    FIN 
```