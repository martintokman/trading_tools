
import sys
import csv

def mostrar_menu_principal():
    print("Menú principal:")
    print("1. Listado de entradas x día")
    print("2. Listado de entradas x activo")
    print("3. Salir")

def menu_principal_1():
    lista = lista_entradas_x_dia()

    while True:
        
        user_input = int(input("Ingrese opción: ")) 
    
        if user_input  > len(lista) or user_input < 1:
            print("Opción no válida, vuelve a intentar.")
            continue
        else:
            break
    
    fecha_a_buscar = lista[user_input - 1]
    print(f"\nFecha a buscar: {fecha_a_buscar}")
    lista_detalle_entradas = mostrar_detalle_entadas_x_fecha(fecha_a_buscar)

    for item in lista_detalle_entradas:
        print(f"Fecha: {item[1]}")
        print(f"Hora: {item[2]}")
        print(f"Activo: {item[3]}")
        print(f"Sesión: {item[4]}")
        print(f"Operación: {item[5]}")
        print(f"Precio de entrada: {item[6]}")
        print(f"Stop loss: {item[7]}")
        print(f"Objetivo: {item[8]}")
        print(f"Lotaje: {item[9]}")
        print(f"Precio de salida 1: {item[10]}")
        print(f"PNL: {item[11]}")
        print(f"Comentarios p. salida 1: {item[12]}")
        print("--------------------------------------")
        print("\n\n")
        

    

def menu_principal_2():
    lista = lista_entradas_x_activo()

    while True:
        
        user_input = int(input("Ingrese opción: ")) 
    
        if user_input  > len(lista) or user_input < 1:
            print("Opción no válida, vuelve a intentar.")
            continue
        else:
            break
    
    activo_a_buscar = lista[user_input - 1]
    print(f"\nActivo a buscar: {activo_a_buscar}")
    lista_detalle_entradas = mostrar_detalle_entadas_x_activo(activo_a_buscar)

    for item in lista_detalle_entradas:
        print(f"Fecha: {item[1]}")
        print(f"Hora: {item[2]}")
        print(f"Activo: {item[3]}")
        print(f"Sesión: {item[4]}")
        print(f"Operación: {item[5]}")
        print(f"Precio de entrada: {item[6]}")
        print(f"Stop loss: {item[7]}")
        print(f"Objetivo: {item[8]}")
        print(f"Lotaje: {item[9]}")
        print(f"Precio de salida 1: {item[10]}")
        print(f"PNL: {item[11]}")
        print(f"Comentarios p. salida 1: {item[12]}")
        print("--------------------------------------")
        print("\n\n")

    




def menu_principal_3():
    print("Goodbye :)")
    sys.exit(0)



        
def convertir_str_a_fecha(fecha):
    from datetime import datetime

    fecha = fecha

    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    return fecha


def lista_entradas_x_dia():
    
    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        #creo una lista de fechas únicas para el menú
        lista = []
        
        #asigno las fechas a la lista y arranco el for a partir
        #de la 2da fila 
        count = 0
        for row in csv_reader:
            if count != 0:
                lista.append(row[1])
            
            count += 1

        
        #elimino cualquier valor en blanco que pueda haber
        #en la lista
        lista2 = []
        for count, item in enumerate(lista):
            if not item:
                pass
            else:
                lista2.append(item)
        lista = lista2
        
        #elimino duplicados
        lista2 = []
        for item in lista:
            if item not in lista2:
                lista2.append(item)
        
        lista = list(lista2)
        
            
        
        #muestro las fechas de la lista en formato menú
        for count, item in enumerate(lista):
            print(f"{count+1}. {item}")
        
    return lista



def lista_entradas_x_activo():
    
    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        #creo una lista de activos para el menú
        lista = []
        
        #asigno los activos a la lista y arranco el for a partir
        #de la 2da fila 
        count = 0
        for row in csv_reader:
            if count != 0:
                lista.append(row[3])
            
            count += 1

        
        #elimino cualquier valor en blanco que pueda haber
        #en la lista
        lista2 = []
        for count, item in enumerate(lista):
            if not item:
                pass
            else:
                lista2.append(item)
        lista = lista2
        
        #elimino duplicados
        lista2 = []
        for item in lista:
            if item not in lista2:
                lista2.append(item)
        
        lista = list(lista2)
        
            
        
        #muestro las fechas de la lista en formato menú
        for count, item in enumerate(lista):
            print(f"{count+1}. {item}")
        
    return lista



def mostrar_detalle_entadas_x_fecha(fecha_a_buscar):

    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        #creo una lista con el detalle de las entradas para
        #la fecha elegida
        lista = []

        #asigno los datos a la lista y arranco el for a partir
        #de la 2da fila 
        count = 0
        for row in csv_reader:
            if count != 0:
                if row[1] == fecha_a_buscar:
                    lista.append(row)
            
            count += 1

    return lista




def mostrar_detalle_entadas_x_activo(activo_a_buscar):

    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        #creo una lista con el detalle de las entradas para
        #la fecha elegida
        lista = []

        #asigno los datos a la lista y arranco el for a partir
        #de la 2da fila 
        count = 0
        for row in csv_reader:
            if count != 0:
                if row[3] == activo_a_buscar:
                    lista.append(row)
            
            count += 1

    return lista


        


