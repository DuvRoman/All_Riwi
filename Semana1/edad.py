import datetime

print("Bienvenido a la calculadora de años \n ")

birthdate= int(input("Ingrese su fecha de nacimiento: "))

date= datetime.datetime.now() 

age= int(date.year) - birthdate

print(f"Su edad actual es: {age} " )

