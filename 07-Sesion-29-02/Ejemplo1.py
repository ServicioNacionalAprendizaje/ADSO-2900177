# Capturar cantidad para cada producto.
a = int(input("Por favor ingrese la cantidad en unidades de arroz que desea llevar: "))
f = int(input("Por favor ingrese la cantidad en unidades de frijol que desea llevar: "))
c = int(input("Por favor ingrese la cantidad en unidades de cereal que desea llevar: "))

# Obtener el valor a pagar por cada producto.
prea = a * 2900
pref = f * 3200
prec = c * 12800

# Obtener el descuento para cada producto
desa = prea*0.97
desf = pref*0.91
desc = prec*0.98

# Obtener el valor final a pagar con y sin descuento
pre = prea + pref + prec
des = desa + desf + desc

# Salida de datos
print("El valor por ", a , " unidades de arroz es ", prea)
print("El valor por ", f , " unidades de frijol es ", pref)
print("El valor por ", c , " unidades de cereales es ", prec)
print("El valor antes de descuento es: ",pre)
print("El valor con descuento es: ",des)





