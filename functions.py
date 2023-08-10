#Functions file
import csv
from entradas_x_dia import *



def function(menu):

    if menu == 1:

        entradas_x_dia()
                
                
                
                
    
    elif menu == 2:
        with open(journal_file) as journal_file:

            journal = csv.reader(journal_file, delimiter=';')
            next(journal)

            print("\n\nEntradas por activo.")
            for row in journal:
                
                print(row[3])

    
    elif menu == 3:
        print("Gracias por usar TradingTools :)")
        exit(0)



   
    
    return user_input
    
    

