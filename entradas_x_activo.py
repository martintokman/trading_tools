#Functions file
import csv



def entradas_x_activo():

    journal_file = "journal.csv"

    
    with open(journal_file) as journal_file:

        journal = csv.reader(journal_file, delimiter=';')
        next(journal)
        
        for row in journal:
            print(row[3])
                