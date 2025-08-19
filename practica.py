# import random

# afirmaciones = [
#     "¡Hoy es un gran día para lograr cosas increibles!",
#     "¡Tienes el poder de crear tu propia realidad!",
#     "¡Cada paso que das te acerca a tus metas!",
#     "¡Eres más fuerte de lo que crees!",
#     "¡El éxito comienza con una mentalidad positiva!",
#     "¡Hoy eliges ser imparable!",
#     "¡Tus posibilidades son infinitas!"
# ]

# afirmacion_del_dia = random.choice(afirmaciones)

# print(f"\033[35mAfirmación del día: {afirmacion_del_dia}\033[0m")

#----------------------------------------------------------------------

#import random
#import time

#def lanzar_dado():
#    return random.randint(1, 6)

#def main():
#    print("\033[33m" + "-" * 40 + "\033[0m")
#   print("    \033[35mBienvenido al simulador de dados\033[0m")
#    print("\033[33m" + "-" * 40 + "\033[0m")

#    while True: 
#        print("\n\033[36m¿Qué quieres hacer?\033[0m")
#        print("1. Lanzar un dado")
#        print("2. Lanzar dos dados")
#        print("3. Salir")
#       print(" ")

#       option = input("\033[32mElige una opción (1-3): \033[0m")

#       if option == "1":
#           resultado = lanzar_dado()
#           print(f"\033[36mHas lanzado un dado y el resultado es: {resultado}\033[0m")
#           time.sleep(3)
#       elif option == "2":
#           resultado1 = lanzar_dado()
#           resultado2 = lanzar_dado()
#           total = resultado1 + resultado2
#           print(f"\033[36mHas lanzado dos dados y los resultados son: {resultado1} y {resultado2}. El total es: {total}\033[0m")
#           time.sleep(3)
#       elif option == "3":
#           print("\033[31m¡Gracias por jugar!\033[0m")
#           break
#       else:
#           print("\033[31mOpción no válida. Por favor, elige una opción del 1 al 3.\033[0m")
#           time.sleep(3)
#           continue
#main()

#----------------------------------------------------------------------

# hola mundo quiero hacer un commit nuevo