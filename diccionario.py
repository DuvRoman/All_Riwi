print("*" * 42)
print("|      INTERACTIVE DICTIONARY PRACTICE     |")
print("*" * 42)
#se crea el arreglo
user_dict = {}
#se crea la sentencia
add_more = "yes"

#Se pone la condicion  y se agregan los contenidos al array
while add_more.lower() == "yes":
    key = input("Enter a key => ")
    value = input("Enter a value => ")
    user_dict[key] = value
    add_more = input("Do you want to add another key-value pair? (yes/no) => ")


#Se leen los resultados al salir del bucle
print("\nHere's your complete dictionary:")
for k, v in user_dict.items():
    print(f"{k}: {v}")