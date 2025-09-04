import math

def potencia(num1, num2):
    return num1 ** num2

def raiz_cuadrada(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Error: numero negativo"

def menu():
    print("\n=== Calculadora ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raiz cuadrada")

while True:
    menu()
    opcion = input("Seleccione una opcion: ")

    elif opcion == "5":
        n1 = float(input("Base: "))
        n2 = float(input("Exponente: "))
        print("Resultado:", potencia(n1, n2))

    elif opcion == "6":
        n1 = int(input("Numero: "))
        print("Resultado:", raiz_cuadrada(n1))

    else:
        print("Opcion no valida, cerrando calculadora.")
        break
