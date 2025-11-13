print("Bienvenido al INVENTARIO")
print("*"*25)

productos = []

while True:
    menu = input("\n Menu: \n 1. Agregar producto \n 2. Mostrar inventario\n 3. Calcular estadísticas \n 4. Salir \n Eliga un numero: ")
    try:
        menu = int(menu)
        if menu > 4 or menu == "":
            print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...")
        
    except ValueError:
        print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...")
      

    while True:
        if menu == 1:
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
            break

        elif menu == 2:
                if not productos:
                    print("No hay productos registrados.")
                else:
                    print(f"\n{'Nombre':<10} | {'Precio':<10} | {'Cantidad':<10}")
                    print("-" * 35)
                for i in productos:
                    print(f"{i['nombre']:<10} | {i['precio']:<10.3f} | {i['cantidad']:<10}")          
                break
    
        elif menu == 3:
            contadorProductos = 0
            totalPrecios = 0
            if not productos:
                print("No hay productos registrados.")
            else:
                print(f"\n{'Valor Total Inventario':<10} | {'Cantidad Total de Productos':<10}")
                print("-" * 35)
            for i in productos:
                contadorProductos = int(i["cantidad"]) + contadorProductos
                totalPrecios = (int(i["precio"])*int(i["cantidad"])) + totalPrecios
            print(f" | {totalPrecios:<10.3f} | {contadorProductos:<20}")
            break

        elif menu == 4:
            print("\n¡¡Gracias por utilizar el inventario¡¡, vuelva pronto")
            exit()



    



        




