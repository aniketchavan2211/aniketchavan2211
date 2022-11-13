#!/bin/python

# Importing SQLite3
import sqlite3

# Connect to Database
conn = sqlite3.connect('Online-Shopping.db')

# Create a Cursor
c = conn.cursor()

# Create a Table
# c.execute("CREATE TABLE clothing( type text, description text, price integer )")

# Creating Python Lists and Tuples
cloths = [
		('shirt', 'oversized,floral pattern', 80),
		('jeans', 'distressed,cropped', 63),
		('dress', 'short, floral embriodery', 55),
		('jacket', 'slim-fit, water proof', 110),
	]

# Inserting Data in Table
# c.executemany("INSERT INTO clothing VALUES (?,?,?)", cloths)

# Query
c.execute("SELECT * FROM clothing WHERE description LIKE '%floral%' ORDER BY price")

# Fetch
values = c.fetchall()
for value in values:
  print (value)

# Display Table
# for cloth in cloths:
#   print (cloth)

# Commit to Database
conn.commit()

# Closing Connection
conn.close()
