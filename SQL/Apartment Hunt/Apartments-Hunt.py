#!/bin/python

import sqlite3

conn = sqlite3.connect('Apartment-Hunt.db')

c = conn.cursor()

# Inserting Values
apartments = [
		('EcoStay', 30),
		('The View', 100),
		('Sunny Place', 53),
		('The Den', 80),
	     ]
#c.executemany("INSERT INTO apartment VALUES (?,?)", apartments)

# Query
c.execute("SELECT * FROM apartment ORDER BY square_meters DESC")



names = c.fetchall()

for name in names:
  print (name)


conn.commit()
conn.close()

