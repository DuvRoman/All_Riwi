# Colores ANSI de fondo
FONDO_VERDE = "\033[42m"
RESET = "\033[0m"

# Imprime un bloque de 10x3 “relleno”
for i in range(3):
    print(FONDO_VERDE + " " * 10 + RESET)

