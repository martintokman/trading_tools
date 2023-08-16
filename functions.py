
import sys
import csv

def show_main_menu():
    print("Main menu:")
    print("1. List trades by date")
    print("2. List trades by asset")
    print("3. Exit")

def main_menu_1():
    _list = list_trades_by_date()

    while True:
        
        user_input = int(input("Select option: ")) 
    
        if user_input  > len(_list) or user_input < 1:
            print("Option invalid, try again.")
            continue
        else:
            break
    
    date_to_find = _list[user_input - 1]
    print(f"\nDate to find: {date_to_find}")
    detailed_trades_list = show_detailed_trades_list_by_date(date_to_find)

    for item in detailed_trades_list:
        print(f"Date: {item[1]}")
        print(f"Time: {item[2]}")
        print(f"Asset: {item[3]}")
        print(f"Session: {item[4]}")
        print(f"Entry type: {item[5]}")
        print(f"Entry price: {item[6]}")
        print(f"Stop loss: {item[7]}")
        print(f"Target: {item[8]}")
        print(f"Volume: {item[9]}")
        print(f"PNL: {item[11]}")
        print(f"Exit price 1: {item[10]}")
        print(f"Comments for exit price 1: {item[12]}")
        print(f"Exit price 2: {item[13]}")
        print(f"Comments for exit price 2: {item[14]}")
        print(f"Entry image: {item[15]}")
        print(f"Structure 1 image: {item[16]}")
        print(f"Structure 2 image: {item[17]}")
        print(f"Trade management: {item[18]}")
        print(f"Trade management image 1: {item[19]}")
        print(f"Trade management image 2: {item[20]}")
        print(f"Trade management image 3: {item[21]}")
        print(f"Trade management image 4: {item[22]}")
        print("--------------------------------------")
        print("\n\n")
        

    

def main_menu_2():
    _list = list_trades_by_asset()

    while True:
        
        user_input = int(input("Select option: ")) 
    
        if user_input  > len(_list) or user_input < 1:
            print("Option invalid, try again.")
            continue
        else:
            break
    
    asset_to_find = _list[user_input - 1]
    print(f"\nActivo a buscar: {asset_to_find}")
    detailed_trades_list = show_detailed_trades_list_by_asset(asset_to_find)

    for item in detailed_trades_list:
        print(f"Date: {item[1]}")
        print(f"Time: {item[2]}")
        print(f"Asset: {item[3]}")
        print(f"Session: {item[4]}")
        print(f"Entry type: {item[5]}")
        print(f"Entry price: {item[6]}")
        print(f"Stop loss: {item[7]}")
        print(f"Target: {item[8]}")
        print(f"Volume: {item[9]}")
        print(f"PNL: {item[11]}")
        print(f"Exit price 1: {item[10]}")
        print(f"Comments for exit price 1: {item[12]}")
        print(f"Exit price 2: {item[13]}")
        print(f"Comments for exit price 2: {item[14]}")
        print(f"Entry image: {item[15]}")
        print(f"Structure 1 image: {item[16]}")
        print(f"Structure 2 image: {item[17]}")
        print(f"Trade management: {item[18]}")
        print(f"Trade management image 1: {item[19]}")
        print(f"Trade management image 2: {item[20]}")
        print(f"Trade management image 3: {item[21]}")
        print(f"Trade management image 4: {item[22]}")
        print("--------------------------------------")
        print("\n\n")

    




def main_menu_3():
    print("Goodbye :)")
    sys.exit(0)



        
def convertir_str_a_fecha(fecha):
    from datetime import datetime

    fecha = fecha

    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    return fecha


def list_trades_by_date():
    
    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        
        #make a list of unique dates for the menu
        _list = []
        
        
        #assign dates to the list and start iterating from the
        #second element of the list
        count = 0
        for row in csv_reader:
            if count != 0:
                _list.append(row[1])
            
            count += 1

        
        
        #delete any possible empty value in the list
        _list2 = []
        for count, item in enumerate(_list):
            if not item:
                pass
            else:
                if item not in _list2:
                    _list2.append(item)
        _list = list(_list2)
        

        #show dates of the list in menu format
        for count, item in enumerate(_list):
            print(f"{count+1}. {item}")
        
    return _list



def list_trades_by_asset():
    
    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        
        #create a list of unique assets for the menu
        _list = []
        
        
        #assing assets to the list and start iterating from the 
        #second element
        count = 0
        for row in csv_reader:
            if count != 0:
                _list.append(row[3])
            
            count += 1

        
        
        #delete any possible empty value in the list
        _list2 = []
        for count, item in enumerate(_list):
            if not item:
                pass
            else:
                if item not in _list2:
                    _list2.append(item)
        _list = _list2
         
        
        
        #show list of dates in menu format
        for count, item in enumerate(_list):
            print(f"{count+1}. {item}")
        
    return _list



def show_detailed_trades_list_by_date(date_to_find):

    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        
        #create a list with trade details for the selected date
        _list = []

        
        #assign data to the list and start iterating from the 
        #second element
        count = 0
        for row in csv_reader:
            if count != 0:
                if row[1] == date_to_find:
                    _list.append(row)
            
            count += 1

    return _list




def show_detailed_trades_list_by_asset(asset_to_find):

    journal_file = "journal.csv"

    with open(journal_file) as journal_file:
        csv_reader = csv.reader(journal_file, delimiter=";")

        
        #create a list with trade details for the selected asset
        _list = []

        
        #assign data to the list and start iterating from 
        #the second element  
        count = 0
        for row in csv_reader:
            if count != 0:
                if row[3] == asset_to_find:
                    _list.append(row)
            
            count += 1

    return _list


        


