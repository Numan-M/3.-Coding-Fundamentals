import sqlite3

def populate_sw_db(character_list):
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        
        for character in character_list:
            name, height, mass, hair_color = character

            # Ensure mandatory field is not empty
            if not name:
                # Skipping entry due to missing name
                continue  

            try:
                # Check if the character already exists (based on name only)
                c.execute("SELECT 1 FROM characters WHERE name = ?", (name,))
                if c.fetchone():
                    # Skipping duplicate entry
                    continue  

                # Convert height to integer if possible, else None
                height = int(height) if str(height).isdigit() else None

                # Insert the new character
                c.execute('''INSERT INTO characters(name, height, mass, hair_color)
                             VALUES(?,?,?,?)''', (name, height, mass, hair_color))
                
            except sqlite3.Error as e:
                # Optionally, handle or log the database error
                pass
            except Exception as e:
                # Optionally, handle or log the unexpected error
                pass
        
        conn.commit()  # Ensure changes are saved


def view_starwars_db():
    '''READ'''
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        for row in c.execute("SELECT * FROM characters"):
            print(row)
    return 

def view_single_entry_starwars_db(search_term, search_item):
    '''READ'''
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        query = f"SELECT * FROM characters WHERE {search_term} = ?"
        c.execute(query, (search_item,))
        result = c.fetchone()
        
    return result 
def delete_starwars_db(char_id):
    '''DELETE ** NEED TO CHANGE QUERY'''
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        c.execute("""
                DELETE FROM characters where id = ?
                """,(char_id,))
        conn.commit()
    return 
def delete_ALL_starwars_db():
    '''DELETE ** NEED TO CHANGE QUERY'''
    with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        c.execute("""
                DELETE FROM characters""")
        conn.commit()
    return 
def update_starwars_db(character):
     id, name, height, mass, hair_color = character
     with sqlite3.connect("starwars.db") as conn:
        c = conn.cursor()
        c.execute('''UPDATE characters
              SET name = ?, height = ?, mass = ?, hair_color = ?
              WHERE id = ?''', (name, height, mass, hair_color, id))
        conn.commit()
        return character
# create_starwars_db()
# chars = extract_starwars_data_from_API()
# populate_sw_db(chars)
# # delete_starwars_db()
# view_starwars_db()

# q=extract_starwars_data_from_API()
# print(q)