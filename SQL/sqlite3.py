#!/bin/python

# Importing SQLite3
import sqlite3

# Connecting to database
conn = sqlite3.connect('database.db')

# Create a cursor
c = conn.cursor()

# Create a Table
# c.execute("""CREATE TABLE table_name( table_column datatype, table_column )""")

 # DATAYPE
 # null - does not exist or exist
 # integer - 1, 2, 3, 4
 # real - 1.5, 8.4
 # text - ABC, abc
 # blob - Img, Audio, Video

# Creating lists & tuples
list_name = [
                ('text/value', real),
                ('text/value', integer),
                ('text/value', number),
                ('text/value', numuber),
             ]

 # Text should enclosed with quotes

# Inserting Data
# c.executemany("""INSERT INTO table_name VALUES (?,?)""", list_name)

# Query
c.execute("SELECT * FROM table_name">

# Updating Data
c.execute("""UPDATE table_name SET table_column='VALUES' WHERE table_column='VALUE' """)

# Delete Data
c.execute("""DELETE FROM table_name WHERE ... """)

# ORDER BY
c.execute("""SELECT rowid,* FROM table_name ORDER BY rowid/Query ASC/DESC""")

# AND/OR
c.execute("""SELECT rowid,* FROM table_name WHERE table_column LIKE '%' AND/OR rowid/Query""")

# Limiting
c.execute("""SELECT rowid,* FROM table_name ORDER BY rowid ASC/DESC LIMIT number/rowid""")

# Drop Table
c.execute("""DROP TABLE table_name""")

# Fetch
values = c.fetchall()
for value in values:
  print (value)

# Show Data from Table
# for list in list_name:
#   print (activity)

# Commit
conn.commit()

# Close connection
conn.close()
