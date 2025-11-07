# Ciclo while para la condicion y el registro dentro de el objeto o lista
#Ciclo for para recorrerlo o imprimirlo

print("Bienvenido a tu listado de Frutas")
print("*"*40)



fruits = []
addfruit= input("Quieres ingresar una fruta: (yes or not)... ")

while addfruit.lower() != "no":
    print("Comandos Erroneos...\n")
    addfruit

    if addfruit.lower() == "yes":
        fruta= input("Ingrese una fruta: ")
        fruits.append(fruta)

    addfruit= input("Quieres ingresar una fruta: (yes or not)... ")



print(f"Su lista es: \n {fruits}" )
print()



