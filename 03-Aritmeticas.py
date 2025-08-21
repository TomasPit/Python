#"""
#    Realiza operaciones aritméticas básicas.
#"""

#print (5+2)
#print (5-2)
#print (5*2)
#print (5%2)
#print (5 ** 2)

#comparaciones
#n1 = 10
#n2 = 15
#print (n1 > n2)
#print (n1 < n2)
#print (n1 >= n2)
#print (n1 <= n2)
#print (n2 == n2)

#Datos de usuario - input y conversion de archivos

#resultado = int(input("Ingresa tu edad: "))
#print(type(resultado))
#print ("Tu edad es", resultado , "y si le sumo dos es: ", resultado + 2)

#Control de flujo - IF

#nota = int(input("Ingresa tu nota: "))
#if nota > 95:
#    print("Aprobado con honores")
#elif nota == 95:
#    print("Aprobado con lo justo")
#else:
#    print("Desaprobado, la proxima será")

#conversor de temperaturas 

temperatura = float(input("Ingrese la temperatura a convertir: "))

caracter = input("Ingrese 'C' para convertir a Celsius o 'F' para convertir a Fahrenheit: ")

if  caracter == 'F' or caracter == 'f':
    temperatura = temperatura + 273
    print("La temperatura en farenheit es: ", temperatura, "°F")
else:
    print("La temperatura es: ", temperatura, "°C")

