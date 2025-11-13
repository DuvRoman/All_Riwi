print("Bienvenido al INVENTARIO")
print("*"*25)

while True:
    menu = input("Menu: \n 1. Agregar producto \n 2. Mostrar inventario\n 3. Calcular estadísticas \n 4. Salir \n Eliga un numero: ")
    try:
        menu = int(menu)
        if menu > 4:
            print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...\n")
            continue
    except ValueError:
        print("\nDatos erroneos, elige un numero... Vuelve a intentarlo...\n")
    
    if menu == 1:
        print("escojiste 1")
        break

    



        




