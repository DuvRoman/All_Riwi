print("Bienvenido a la calculadora de precio")
print("*" * 40)


while True:
    NombreDelProducto = input("Ingresa el nombre del producto: ").strip()
    if NombreDelProducto.isalpha() or " " in NombreDelProducto:
        break
    else:
        print("Dato erróneo... el nombre debe contener solo letras.\n")


while True:
    precio= input("Ingresa el precio de el producto: ")
    try:
        precio = float(precio)
        break
    except ValueError:
        print("Datos erroneos, solo se pueden ingresar numeros.. Vuelve a intentarlo\n")
        

while True:
    cantidad= input("Ingresa la cantidad de el producto: ")
    try:
        cantidad = int(cantidad)
        break
    except ValueError:
        print("Datos erroneos, solo se pueden ingresar numeros... vuelve a intentarlo\n")

costoTotal= precio * cantidad

print(f"\nProducto: {NombreDelProducto} | Precio: {precio} | Cantidad:{cantidad} | Total: {costoTotal} ")
