usuarioRBP = "Facundo"
passwordRBP = 'Faku2109'
saldo = 15000

def validarUsuario(u,p):
    if u == usuarioRBP and p == passwordRBP:
        return True
    return False

def login():
    print('Bienvenido')
    usuario = input('Digite el usuario: ')
    password = input('Digite la contraseña: ')
    return validarUsuario(usuario, password)

def retirar(valor):
    if valor > saldo:
        return False, saldo
    return True, saldo - valor

def depositar(valor):
    return True, saldo + valor

def accion(opcion):
    while True:
        if opcion == 1:
            valor = int(input('Digite el valor que depositara: '))
            return depositar(valor)
        if opcion == 2:
            valor = int(input('Ingrese el valor a retirar: '))
            return retirar(valor)
        if opcion == 3:
            print('Gracias por usar el sistema')
            break
        else:
            print('Opcion invalida, intente de nuevo.')
    return False, saldo

def ejecutar():
    while True:
        if not login():
            print('Usuario o clave incorrectos, intente otra vez.')
        else:
            print('Que Operacion desea realizar?')
            opcion = int(input("\n1 Depositar  \n2. Retirar saldo \n3 Salir \n. "))
            ok, saldo = accion(opcion)
            if not ok:
                print('No se ha podido realizar la accion, saldo: ', saldo)
            else:
                print('Accion realizada correctamente, saldo ', saldo)
                break
ejecutar()
