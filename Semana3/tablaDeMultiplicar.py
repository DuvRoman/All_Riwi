number = int(input("Ingrese el numero de su tabla: "))

with open ("Semana3/table.txt", "w") as table:
    for i in range(1,11):
        table.write(f"{number} x {i} = {number * i} \n")


