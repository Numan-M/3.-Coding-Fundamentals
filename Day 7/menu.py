# 4. Create a Command-Line Menu System
# •	Build a command-line interface (CLI) where users can interact with the system and perform CRUD operations.
# •	The menu should allow the following options:
# o	1View all records: Display a list of all records in the database.
# o	2Search records by ID: Allow the user to input an ID and retrieve a specific record.
# o	3Search records by name: Implement a search option that allows users to input a name and find the corresponding record.
# o	4Update a record: Allow the user to update an existing record by specifying the record’s ID.
# o	5Delete a record: Allow the user to delete a record based on its ID.
# o	Exit: Exit the program.
import time
import os



def menu():
        time.sleep(0.5)
        try:    
            option = int(input('''
---  STAR WARS  ---

1. View all records
2. Search record 
3. Update record
4. Delete record
5. Exit
                               
Enter: '''))
            os.system('cls' if os.name == 'nt' else 'clear')
        except ValueError:
            print('\nERROR: Invalid input. Please enter a number between 1 and 5.')
            time.sleep(3)
        
        return option
