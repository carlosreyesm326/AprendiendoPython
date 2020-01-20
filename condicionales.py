


num = float(input("Ingrese un numero: "))


if num > 0:

	print("Es un numero positivo")

elif num == 0:

	print("El numero es 0")

else: 
	print("el numero es negativo")	

	
	#Ejercicios 1

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

if a%2 == 0 and b%2 == 0:

	print("Ambos numeros son pares")

elif a%2 == 0 and b%2 !=0 :

	print("A es par y B impar")

elif a%2 != 0 and b%2 == 0:

	print("Solo B es par")

else:

	print("Ninguno de los dos numeros es par")

print("FINAL")

	

	#Ejercicios 3

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

if a<b and b<c:

	print(f"C es el mayor numero {c}")

elif a<b and b>c:

	print(f"B es el mayor numero {b}")
else:

	print(f"A es el mayor numero: {a}")





	#Ejercicios 3

letra = input("Ingrese una letra: ").lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":

	print(f"La letra {letra} es una vocal")

else:
	print(f"La letra {letra} no es una vocal")

