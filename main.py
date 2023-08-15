import csv, os, sys
from functions import *

os.system("clear")

while True: #restart

    print("Menú principal:")
    print("1. Listado de entradas x día")
    print("2. Listado de entradas x activo")
    print("3. Salir")
    menu = int(input("\n\nIngrese una opción: "))

    if menu == 1:
        #functions.py
        menu_entradas_x_dia(menu)

        print("holi")

    if menu == 3:
        print("Goodbye :)")
        sys.exit(0)

    
    tecla = input("\nPresione una tecla para continuar.")
    os.system("clear")
    continue


    
    


  


   
            




