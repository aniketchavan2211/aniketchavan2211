#!/bin/python

# Importing SQLite3
import sqlite3

# Connecting to Database
conn = sqlite3.connect('Analyze-Survey-Data.db')

# Creating A Cursor
c = conn.cursor()

# Creating A Table
# c.execute("CREATE TABLE survey( platform text, satisfaction integer)")

# Python Lists and Tuples
survey_table = [
		('desktop', 4),
		('iOS', 6),
		('andriod', 7),
		('desktop', 5),
		('andriod', 3),
		]
# Inserting Values in Database
c.executemany("""INSERT INTO survey VALUES (?,?)""", survey_table)

# Query
c.execute("SELECT DISTINCT platform FROM survey WHERE satisfaction  BETWEEN 4 AND 6;")

# Fetch
print (c.fetchall())

# Display Table
# print ("-----------------------")
# print ("Show Table")
# for survey in survey_table:
#   print (survey)

# Commitng to Database
conn.commit()

# Closing Connection
conn.close()
