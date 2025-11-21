
def menu():

    while True:
        menu= input("\n Menu: \n 1. Agregar producto \n 2. Mostrar inventario\n 3. Calcular estadísticas \n 4. Salir \n Escoja un numero: ")
       
        try:
            menu = int(menu)
            if menu > 4 or menu == "":
                print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...")  
                 
        except ValueError:
            print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...")
    
        return menu 
            
    

def agregarProductos(productos):
    opcion = menu()
    while True:
        if opcion == 1:
            name = input("Ingrese el nombre de el producto: ")
            if name.isnumeric() or name == "":
                print("\nDatos erroneos, Debes ingresar letras... Vuelve a intentarlo...")
                break
            precio = input("Ingrese el precio de el producto: ")
            try:
                precio = float(precio)
            except ValueError:
                ("\nDatos erroneos, desbes ingresar numeros... Vuelve a intentarlo...")
                break
            cantidad= input("Ingrese la cantidad de el producto: ")
            try:
                cantidad = int(cantidad)
            except ValueError:
                ("\nDatos erroneos, desbes ingresar numeros... Vuelve a intentarlo...")
                break            
            
            producto = {
                "nombre": name,
                "precio" : precio,
                "cantidad" : cantidad
            }
            productos.append(producto)
            print(f"Producto agregado correctamente")
            break
