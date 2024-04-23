def calcularIMP(p):
    IMP = p * 0.08
    return IMP

def calcularIVA(i):
    IVA = i * 0.21
    return IVA

def calcularGAN(g):
    GAN = g * 0.30
    return GAN
# primer while para preguntar si se ingresa otro valor
# segundo while por si el usuario ingresa cualquier cosa menos un numero
while True:
    while True:
        try:
            precioCompra = float(input("Ingresar el precio de la compra: "))
            break
        except ValueError:
            print("Por favor solo ingresar numeros")
    IMP = calcularIMP(precioCompra)
    IVA = calcularIVA(precioCompra)
    GAN = calcularGAN(precioCompra)
# en el prin se suman el resultado de cada operacion echa arriba y da el resultado (añadir que ponga 2 desimales nomas)
    print("El valor de la compra con impuestos es de:",(precioCompra+IMP+IVA+GAN))
    respuesta = input("¿Desea ingresar otro valor? S para si o N para no: ").lower()
    if respuesta == "n":
        break