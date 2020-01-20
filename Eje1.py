
import math

#ejercicio 1

print("----------------------------------------------------")
print("resultado de la evaluacion de uan funcion cuadratica")
print("----------------------------------------------------")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

print("----------------------------------------------------")
print("\t Analizando...")
print("----------------------------------------------------")

rel= ((a**a)*(b**2-2*a*c))/(2*b)

print(f"El resultado es: \n -> {rel}")


#Ejercicio 2

print("----------------------------------------------------")
print("resultado de una evaluacion logica")
print("----------------------------------------------------")

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))


bo = ((3+5*8)<3	and (((-6/3)*4)+2<2)) or (a>b)

print(f"El valor es: {bo}")

#Ejercicio 3

print("----------------------------------------------------")
print("\t Intercambiar variables")
print("----------------------------------------------------")


a = float(input("Ingrese el valor de A: "))

b = float(input("Ingrese el valor de B: "))


Cache = a 

print(f"El valor actual de A es: {a}, el valor de B actual es: {b} \n")
print("----------------------------------------------------")
print("\t Analizando...")
print("----------------------------------------------------")

a=b
b=Cache

print(f"El valor nuevo de A es: {a}, el valor de B ahora es: {b}")


radio = float(input("Ingrese el raio: "))

longitud =   2*radio*math.pi 
Area = math.pi*radio**2

print(f"La longitud es: {longitud:.2f} y el Area es: {Area:.2f}")


#Ejercicio 5

print("----------------------------------------------------")
print("\t Descuento")
print("----------------------------------------------------")


valor = float(input("Ingrese el valor a pagar: "))


ope = valor - valor*0.15

print(f"El valor a pagar es: {ope}") 