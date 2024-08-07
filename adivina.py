numero = 7
usuario = 0
while usuario != numero:
    usuario = int(input('Cual es el numero?'))
    if usuario > numero:
        print('Digite un numero menor')
    elif usuario < numero:
        print('Digite un numero mayot')
    else:
        print('Correcto')