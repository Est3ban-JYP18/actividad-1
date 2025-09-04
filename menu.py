def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

elif opcion == "1":
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print("Resultado:", suma(n1, n2))

elif opcion == "2":
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))
    print("Resultado:", resta(n1, n2))
