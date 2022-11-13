#!/bin/python

# Importing SQLite3 Module
import sqlite3

# Connect to database
conn = sqlite3.connect('Activity-Booking.db')

# Create a cursor
c = conn.cursor()

# Create a Table
# c.execute("CREATE TABLE activity( description text, type text, price integer)")

# Creating lists & tuples
activities = [
		('kayaking', 'water', 180),
		('skydiving', 'air', 250),
		('scuba diving', 'water', 270),
		('safari', 'land', 150),
	     ]

# Inserting record into the table
# c.executemany("INSERT INTO activity VALUES (?,?,?)", activities)

# Query
c.execute("SELECT description, price FROM activity WHERE type <>'water'")

# Fetch
print (c.fetchall())

# Show All Values from Table
# for activity in activities:
#   print (activity)

# Commit
conn.commit()

# Close connection
conn.close()


