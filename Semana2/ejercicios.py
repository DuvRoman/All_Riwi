
# def impuestos(precio, iva=19):
#     iva= precio * (iva/100)
#     return precio + iva


# print("La camisa con IVA incluido queda en : ", impuestos(150), "$")


def promedio(*numeros):

    contador = 0
    totalLista = 0

    if numeros != ():
        for i in numeros :
            contador += 1
            totalLista = i + totalLista 

    else:
        return print("El resultado es: 0")


    promedio = float(totalLista / contador)

    return print(f"El promedio de la lista es : {promedio}")

promedio(15,15)





