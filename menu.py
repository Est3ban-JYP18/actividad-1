def multiplicacion (num1 ,num2):
    return num1 * num2
    
def main () :
    print ("multiplicacion") 

def division (num1, num2):
    return num1 / num2

def main () :
    print ("division")

num1 = int(input("digite numero 1 :"))
num2 = int(input("digite numero 2 :"))

resultado = multiplicacion(num1, num2)
print("el resultado es: ", resultado)

resultado= division(num1, num2)
print("el resultado es: ", resultado)