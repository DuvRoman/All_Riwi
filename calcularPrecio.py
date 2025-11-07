print("Bienvenido a la calculadora de precio")
print("*" * 40)

 
NombreDelProducto= input("Ingresa el nombre de el producto: ")
precio= float(input("Ingresa el precio de el producto: "))
cantidad= int(input("Ingrese la cantidad de el producto: "))



# if NombreDelProducto != str:
#    NombreDelProducto= input("Ingresa el nombre de el producto: ")
    
# precio= float(input("Ingresa el precio de el producto: "))
# if type(precio) != float:
#     print("Datos erroneos.. vuelve a intentarlo \n")
#     precio= float(input("Ingresa el precio de el producto: "))
    
# cantidad= int(input("Ingrese la cantidad de el producto: "))
# if type(cantidad) != int:
#     print("Datos erroneos.. vuelve a intentarlo \n")
#     cantidad= int(input("Ingrese la cantidad de el producto: "))

costoTotal= precio * cantidad

print(f"Producto: {NombreDelProducto} | Precio: {precio} | Cantidad:{cantidad} | Total: {costoTotal} ")

#Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500