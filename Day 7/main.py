from menu import menu
import time
from starwarsDB import create_starwars_db
from starwarsAPI import extract_starwars_data_from_API
from crud_operations import *
import os
if __name__ == "__main__":
    create_starwars_db()
    extract_result = extract_starwars_data_from_API()
    print(extract_result)
    time.sleep(1.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        time.sleep(1)
        choice = menu()
        match choice:
            case 1:
                # View
                print("--- View all records ---")
                view_starwars_db()
            case 2:
                # Search
                print("--- Search record ---")
                search_choice = int(input('''
1. ID
2. Name

Enter: '''))
                
                if search_choice == 1:
                    char_id = input('Enter ID: ')
                    print(view_single_entry_starwars_db('id',char_id))
                    
                elif search_choice == 2:
                    char_name = input('Enter Name: ')
                    print(view_single_entry_starwars_db('name', char_name))
                    
                else:
                    print('ERROR: Option not in range\nPlease enter 1 or 2')
            case 3:
                # Update
                print("--- Update record ---")
                view_starwars_db()
                update_char_by_id = int(input('Select Id: '))
                id_char_tuple = view_single_entry_starwars_db('id',update_char_by_id)
                name_new = input('Name: ')
                height_new = int(input('Height: '))
                mass_new = input('Mass: ')
                hair_color_new = input('Hair color: ')
                char_new_tup = (id_char_tuple[0],name_new, height_new, mass_new, hair_color_new)
                print(update_starwars_db(char_new_tup))
            case 4:
                # Delete
                print("--- Delete record ---")
                view_starwars_db()
                del_char_by_id = int(input('Select Id: '))
                print(view_single_entry_starwars_db('id',del_char_by_id), 'Has been removed')
                delete_starwars_db(del_char_by_id)
                
            case 5:
                # Exit
                print('--- Exit --- \nGoodbye!')
                break
            
            case 6:
                delete_ALL_starwars_db()
            case _:
                print("\nERROR: Option not in range\nPlease enter a number between 1 and 5.")
                time.sleep(3)
    