# import requests
# import sqlite3
# def extract_starwars_data_from_API():
#     characters = []
#     base_url = 'https://swapi.dev/api/people/?page='
#     for i in range(1,10):
#         url = f'{base_url}{i}'
#         response = requests.get(url)
#         if response.status_code == 200:
#             data = response.json()
#             for character in data['results']:
#                 char_name = character['name']
#                 char_height = int(character['height']) if character['height'].isdigit() else ''
#                 char_mass = character['mass']
#                 char_hair_color = character['hair_color']
#                 characters.append((char_name,char_height,char_mass,char_hair_color))
#     with sqlite3.connect("starwars.db") as conn:
#         c = conn.cursor()
#         for character in characters:
#             name, height, mass, hair_color = character

#             # Ensure mandatory field not empty
#             if not name:
#                 print(f"Skipping entry due to missing data: {character}")
#                 continue  # Skip this entry

#             try:
#                 # Check if the character already exists (based on name)
#                 c.execute("SELECT 1 FROM characters WHERE name = ? AND height = ? AND mass = ? AND hair_color = ?", (name,height, mass, hair_color))
#                 if c.fetchone():
#                     print(f"Skipping duplicate entry: {name}, {height}, {mass}, {hair_color}")
#                     continue  # Skip the duplicate entry

#                 # Insert the new character
#                 c.execute('''
#                     INSERT INTO characters(name, height, mass, hair_color)
#                     VALUES(?,?,?,?)''', (name, height, mass, hair_color))
                
#             except sqlite3.Error as e:
#                 print(f"Database error: {e}")
#             except Exception as e:
#                 print(f"Unexpected error: {e}")
        
#         conn.commit()
#     return 

import requests
import sqlite3

def extract_starwars_data_from_API():
    """Fetch Star Wars characters from the API and populate the database, ensuring no duplicates based on all fields."""
    
    characters = []
    base_url = 'https://swapi.dev/api/people/?page='
    
    # Fetch data from the API
    for i in range(1, 10):
        response = requests.get(f'{base_url}{i}')
        if response.status_code == 200:
            data = response.json()
            for character in data['results']:
                char_name = character['name']
                # Convert height to integer if possible, else None
                try:
                    char_height = int(character['height']) if character['height'].isdigit() else None
                except ValueError:
                    char_height = None
                char_mass = character['mass']
                char_hair_color = character['hair_color']
                characters.append((char_name, char_height, char_mass, char_hair_color))
    
    # Insert data, handling NULLs properly in duplicate checks
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        
        for char in characters:
            name, height, mass, hair_color = char
            
            # Build the query dynamically to handle NULL in height
            query = "SELECT COUNT(*) FROM characters WHERE name = ? "
            params = [name]
            
            if height is None:
                query += "AND height IS NULL "
            else:
                query += "AND height = ? "
                params.append(height)
            
            query += "AND mass = ? AND hair_color = ?"
            params.extend([mass, hair_color])
            
            c.execute(query, params)
            count = c.fetchone()[0]
            
            if count > 0:
                continue  # Skip duplicate
            
            try:
                c.execute("""
                    INSERT INTO characters (name, height, mass, hair_color)
                    VALUES (?, ?, ?, ?)
                """, (name, height, mass, hair_color))
            except sqlite3.Error as e:
                print(f"Error inserting {name}: {e}")
        
        conn.commit()
    
    return {"message": "Database updated, duplicates skipped."}

