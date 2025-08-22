# creando una lista (se pueden modiicar)

lista = ["soy pita","Tomas,","23 años","Argentino-Italiano"]

print(lista[3])

#creando una tupla (no se pueden modificar)

tupla = ("soy pita","Tomas,","23 años","Argentino-Italiano")

print(tupla[2])

#creando un conjunto (set) (no se accede a los elementos por indice, no almacena datos duplicados )

conjunto = {"soy pita","Tomas,","23 años","Argentino-Italiano"}

#print(conjunto[1]) -> no se puede acceder al elemento

print(conjunto)

#creando un diccionario (dict)
diccionario = {
    'nombre': "Tomás Pitavino",
    'edad': 23,
    'altura': 1.76 
}
print(diccionario['altura'] ) 


print ("operadores logicos")

#AND

condicion1 = True and True #return true
condicion2 = True and False #return false
condicion3 = False and True #return false
condicion4 = False and False #return true

#OR

condicion5 = True or True #return true
condicion6 = True or False #return true
condicion7 = False or True #return true
condicion8 = False or False #return false

#NOT

condicion9 = not True #return false
condicion10 = not False #return true

print (condicion1)


#AND

condicion1 = True and True #return true
condicion2 = True and False #return false
condicion3 = False and True #return false
condicion4 = False and False #return false

#OR

condicion5 = True or True #return true
condicion6 = True or False #return true
condicion7 = False or True #return true
condicion8 = False or False #return false

#NOT

condicion9 = not True #return false
condicion10 = not False #return true

#-------------------------------------------------
#Metodos - Metodos de cadena

cadena1 = "Hola Bostero"
cadena2 = "MAÑANA JUEGA BOKITA"
cadena3 = "hoy juga boca"

#convierte a mayusculas
resultado1 = cadena1.upper()

#convierte a minusculas
resultado2 = cadena2.lower()

resultado3= dir(cadena1)


print (resultado1)
print (resultado2)
print (resultado3)
print (cadena3.capitalize())

#busca una cadena en otra cadena y si no hay concidencias devuelve -1

busqueda_find = cadena1.find("Bostero")
print(busqueda_find)

#busca una cadena en otra cadena y si no hay concidencias
busqueda_index = cadena1.index("o")
print(busqueda_index)