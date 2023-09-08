#************* VER COMO IMPLEMENTAR DATA FRAMES PARA MEJORAR ****************
#************* LA LEGIBILIDAD Y DESPUES AGREGAR LA FUNCIÓN ******************
#*************        EDITAR JOURNAL


from params import *
import sys
import csv
import pandas as pd
import numpy as np
import os

def show_main_menu():
    print()
    print("Main menu:")
    print("1. List trades by date")
    print("2. List trades by asset")
    print("3. Edit trading journal")
    print("4. Exit")




def main_menu_1():


    os.system("clear")
    print()
    print("List trades by date")
    #return menu dataframe
    menu = menu_list_trades_by_date()
    #set index to orderer numbers for menu items
    menu.index = [x for x in range(1, len(menu)+1)]

    #format date to dd-mm-yyyy and show menu
    for count, item in enumerate(menu):
        item = item.strftime("%d-%m-%y")
        print(f"{count+1}. {item}")

    return menu
    



    

def main_menu_2():

    menu = list_trades_by_asset()

    for count, item in enumerate(menu):
         if not isinstance(item, float):
             print(f"{count+1}. {item}")

    
    
def main_menu_3():
   pass


def main_menu_4():
    print("Goodbye :)")
    sys.exit(0)



def menu_list_trades_by_date():
    #read journal
    journal = pd.read_excel(journal_file, sheet_name="backup")
    
    #generate array with unique values of asset
    menu = journal["Fecha"]
    
    #remove duplicates
    menu = menu.drop_duplicates()
    
    return menu

def list_trades_by_date(date_to_find):
    #read journal
    journal = pd.read_excel(journal_file, sheet_name="backup")
    
    list_of_trades = journal[journal["Fecha"] == date_to_find]
    list_of_trades = list_of_trades[["Fecha", "Hora", "Activo", "Operación", "PNL %", "P. entrada", "S. loss"]]
    list_of_trades.index = [x for x in range(1,len(list_of_trades)+1)]
    
    return list_of_trades
    



def list_trades_by_asset():
    #read journal
    journal = pd.read_excel(journal_file, sheet_name="backup")
    
    #generate array with unique values of asset
    menu = journal["Activo"]
    
    #remove duplicates
    menu = menu.drop_duplicates()
    
    return menu

    




