print("\n¿Será que puedes ingresar a la discoteca?\n")

edad = int(input("Ingresa tu edad: "))

boleto= input("\nTienes el boleto: (si o no)...")

if edad >= 18 and boleto.lower() == "si":
    print("\n ¡¡Puedes ingresar!!")
else:
    print("\n Eres menor de edad Devuelva el boleto pa revenderlo y .. \n ¡¡Pa la casa gonorrea!!\n")
        