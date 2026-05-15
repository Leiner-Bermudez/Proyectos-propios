#Calculadora basica en python
nombre = ("___Calculadora___")
print(nombre)
operacion = input("que operacion deseas realizar:")
num1 = float(input("Digita el primer numero:"))
num2 = float(input("Digita el segundo numero:"))
if operacion == "suma" or operacion == "+":
    print("Resultado:", num1 + num2)
elif operacion == "resta" or operacion == "-":
    print("resultado:", num1 - num2)
elif operacion == "multiplicacion" or operacion == "*":
    print("Resultado:", num1 * num2)
elif operacion == "division" or operacion == "/":
    if num2 ==0:
        print("no se puede dividir")
    else: print("Resultado:", num1 / num2)