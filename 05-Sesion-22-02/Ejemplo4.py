#1.2.5.	El dueño de una tienda compra un artículo a un 
# precio determinado. Obtener el precio en que lo debe vender 
# para obtener una ganancia del 30%.

precio_articulo = 0 
ganancia = 0
precio_final = 0

precio_articulo = float(input("indique el precio que tiene el producto: "))
ganancia= precio_articulo*0.3
precio_final = precio_articulo + ganancia

#Salida del proceso
print("POr un artículo que le costo "+str(precio_articulo)+", lo venderá por "+str(precio_final))





