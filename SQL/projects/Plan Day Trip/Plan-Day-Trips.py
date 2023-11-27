#!/bin/python

# Importing SQLite3 Module
import sqlite3

# Connecting to Database
conn = sqlite3.connect('Plan-Day-Trips.db')

# Creating a Cursor
c = conn.cursor()

# Creating Table
# c.execute("CREATE TABLE day_trip( destination text, minutes_away integer)")

# Python list and tuples
trips = [
	 ('Ostia Antica', 25),
	 ('Napla', 75),
	 ('Tivoli', 50),
	 ('Florence', 90),
	]

# Inserting Records into table
# c.executemany("INSERT INTO day_trip VALUES (?,?)", trips)

# Query
c.execute("SELECT destination FROM day_trip WHERE minutes_away <= 60")

# Fetch
Result = (c.fetchall())
print (Result)

# Show Table
# (Make sure you you make Query and Fetch comment or remove from program)
# c.execute("SELECT * FROM day_trip")
# for trip in trips:
#   print (trip)

# Commit to Database
conn.commit()

# Connection Close
conn.close()
