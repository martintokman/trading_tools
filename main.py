import csv, os, sys
from functions import *


os.system("clear")

while True: #restart

    show_main_menu()
    user_input = int(input("\n#"))
    
    if user_input == 1: #List trades by date
        while True: #List trades by date
            #show menu
            menu = main_menu_1()


            user_input = (input("\n#"))

            if user_input == "m": #main menu
                os.system("clear")
                
                break
            else:
                user_input = int(user_input)

        
            
                
            #create list based on date_to_find    
            date_to_find = menu[user_input]
            list_of_trades = list_trades_by_date(date_to_find)


            #show results
            os.system("clear")
            print("")

            print(list_of_trades)


            user_input = input("\n#")

            if user_input == "m": #main menu
                os.system("clear")
                break
            elif user_input == "b": #before (previous screen)
                user_input = 1
                continue


        
        














    
    if user_input == 2:
        main_menu_2()

    if user_input == 3:
        main_menu_3()
        
    
    if user_input == 4:
        main_menu_4()
    



    
        


    
    


  


   
            




