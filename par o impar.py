while True:
    try:
        num1 = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

while True:
    try:
        num2 = int(input("Ingrese otro número: "))
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2 !=0:
    print (f"{num1} es par")
elif num1%2 !=0 and num2%2==0:
    print(f"{num2} es par")
else:
    print("Ambos numero son impares")