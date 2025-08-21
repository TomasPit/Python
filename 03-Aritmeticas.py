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

#temperatura = float(input("Ingrese la temperatura a convertir: "))

#caracter = input("Ingrese 'C' para convertir a Celsius o 'F' para convertir a Fahrenheit: ").lower()

#if   caracter == 'f':
#    temperatura = temperatura + 273
#    print("La temperatura en farenheit es: ", temperatura, "°F")
#elif  caracter == 'c':
#    print("La temperatura es: ", temperatura, "°C")
#else:
#    print("Caracter no válido")

#print("¡Gracias por usar nuestro conversor!")

#Listas

#lenguajes = ["Python", "Ruby", "PHP" ,"JavaScript","Java"]
#print(lenguajes, "- El segundo elemento sin cambiar")
#lenguajes[1] = "GO"
#print(lenguajes, "- El segundo elemento ha cambiado\n")

#print(lenguajes[1:3])
#print(lenguajes[:3])
#print(lenguajes[1:])

#metodos de una lista
#lenguajes = ["Python", "Ruby", "PHP" ,"JavaScript","Java"]
#lenguajes.insert(3, "GO")
#lenguajes.insert(0, "C")
#lenguajes.remove("ruby")
#print("PHP" in lenguajes)
#print(len(lenguajes))

# Bucles While 

#lenguajes = ["Python", "Ruby", "PHP" ,"JavaScript","Java"]

#i = 0 
#while i < len(lenguajes):
#    print(lenguajes[i])
#    i = i + 1

#Bucles For

#lenguajes = ["Python", "Ruby", "PHP" ,"JavaScript","Java"]

#for i in lenguajes:
#    print(i)

