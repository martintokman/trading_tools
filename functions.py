
import sys
import csv


def menu_entradas_x_dia(menu):
    if menu == 1:
        mostrar_entradas_x_dia()

        

    if menu == 3:
        print("Goodbye :)")
        sys.exit(0)
        
def convertir_str_a_fecha(fecha):
    from datetime import datetime

    fecha = fecha

    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    return fecha


def mostrar_entradas_x_dia():
    
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

        


