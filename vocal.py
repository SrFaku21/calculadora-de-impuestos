letra = input('Digite un caracter: ').lower()

if letra.isalpha():
    if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
        print('Es una vocal')
    else:
        print('No es una vocal')
else:
    print('Por favor solo ingresar letras')