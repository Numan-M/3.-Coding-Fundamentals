
# Day 7 Project: Star Wars API Integration with SQLite Database

This project interacts with the Star Wars API (SWAPI), stores character data in an SQLite database, and provides CRUD operations through a command-line interface.

---

## 1. **API Overview**  
**Chosen API**: [SWAPI (Star Wars API)](https://swapi.dev/)  
**Data Provided**:  
The API returns character data including:
- `name` (string)
- `height` (integer or null)
- `mass` (string - handles 'unknown' values)
- `hair_color` (string)

Example response structure:
```json
{
    "name": "Luke Skywalker",
    "height": "172", 
    "mass": "77",
    "hair_color": "blond"
}
```

---

## 2. **SQLite Database Structure**  
Database: `starwars.db`  

### Table: `characters`
| Column        | Type        | Description                          |  
|---------------|-------------|--------------------------------------|  
| `id`          | INTEGER     | Primary key, auto-incremented        |  
| `name`        | TEXT        | Character name (required)            |  
| `height`      | INTEGER     | Height in cm (nullable)              |  
| `mass`        | TEXT        | Mass in kg (handles 'unknown')       |  
| `hair_color`  | TEXT        | Hair color description               |  

---

## 3. **CRUD Operations**  
### Key Functions:
- **Create**  
  - `extract_starwars_data_from_API()`: Fetches data from 9 pages of SWAPI (`people/?page=1-9`)
  - Handles data conversion:  
    - `height` → integer (or `NULL` if invalid)  
    - Prevents duplicates using composite checks (name, height, mass, hair_color)

- **Read**  
  - `view_starwars_db()`: Shows all characters
  - `view_single_entry_starwars_db()`: Search by ID or name

- **Update**  
  - `update_starwars_db()`: Modify all fields by ID
  - Preserves original ID while updating other attributes

- **Delete**  
  - `delete_starwars_db()`: Remove by ID
  - `delete_ALL_starwars_db()`: Clear entire table (hidden option)

**Database Interaction**:  
- Uses context managers (`with sqlite3.connect()`) for connection handling
- Parameterized queries prevent SQL injection

---

## 4. **User Interface**  
Command-line menu system with these options:

1. **View All Records**  
   - Displays all characters in database table format

2. **Search Records**  
   - Choose search by:  
     - **ID**: Exact match
     - **Name**: Exact match (case-sensitive)

3. **Update Record**  
   - View all → Select ID → Update:  
     - Name (required)
     - Height (integer validation)
     - Mass (free text)
     - Hair color (free text)

4. **Delete Record**  
   - View all → Select ID → Confirm deletion

5. **Exit**  
   - Clean exit with goodbye message

6. **Delete All** (hidden option)  
   - Clears entire database table

**UI Features**:  
- Automatic screen clearing after actions
- Input validation for numeric fields
- Error handling for invalid menu choices
- 1-second delays for smooth interactions

---

## Setup & Usage
1. **Requirements**:  
   - Python 3.x
   - `requests` library (`pip install requests`)

2. **Run**:  
   ```bash
   python main.py
   ```
   - Database (`starwars.db`) created automatically
   - Initial API data fetched on first run

3. **Notes**:  
   - Duplicate characters are automatically skipped during initial population
   - Mass field preserves original API values (including 'unknown')
   - Height stored as integer where possible, otherwise `NULL`

[View Project Repository](https://github.com/Numan-M/3.-Coding-Fundamentals/tree/main/Day%207)
