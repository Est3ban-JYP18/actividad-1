def suma (num1 ,num2):
    return num1 + num2

def main ():
    print(suma)

def resta (num1 ,num2):
    return num1 - num2

def main ():
    print(resta)



num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))


resultado = suma(num1, num2)
print("El resultado de la suma es:", resultado)

resultado = resta(num1, num2)
print("El resultado de la resta es:", resultado)
