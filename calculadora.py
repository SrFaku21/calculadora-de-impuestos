num1 = float(input('Digite un numero: '))
num2 = float(input('Digite otro numero: '))

operacion = input('Elija la operacion: ').lower()

if operacion=='s':
    suma = num1+num2
    print(f'\nLa Suma es: {suma}')
elif operacion == 'r':
    resta = num1-num2
    print(f'\nLa Resta es: {resta}')
elif operacion =='m' or operacion=='p':
    mult = num1*num2
    print(f'\nLa Multiplicacion es: {mult}')
elif operacion== 'd':
    div = num1/num2
    print(f'\nLa Division es: {div:.4f}')
else:
    print('\nOperacion equivocada')
# .2f muestra decimales de acuerdo al num
# f'\n permite insertar texto y una interpolacion osea hacer algo dif al string1