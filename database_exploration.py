#> database_exploration.py

import os
from dotenv import load_dotenv
import sqlite3

load_dotenv() #> loads contents of the .env file into the script's environment

# construct a path to the database
#DB_FILEPATH = "chinook.db"

DB_FILEPATH = os.getenv("DB_FILEPATH")

connection = sqlite3.connect(DB_FILEPATH)
# connection.row_factory = sqlite3.Row # results like objects instead of tuples
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query = """
SELECT * from database
    LIMIT 10;
"""

cursor.execute(query)
result = cursor.fetchall()
print("RESULT:", type(result))
print(result)

cursor.close()
connection.close()