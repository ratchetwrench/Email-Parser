import sqlite3
import sys

# TODO: sqlite3 - schema, connection, database, tables
# TODO: Create Connection
connection = sqlite3.connect('email.db') # Connect or create database
try:
    with connection:
        # TODO: Create Tables
        # Create notification table
        connection.execute('''CREATE TABLE notification
                           (_id INT AUTOINCREMENT NOT NULL,
                           incident_number TEXT PRIMARY KEY NOT NULL,
                           category TEXT,
                           customer_impact TEXT,
                           content BLOB,
                           notification_date TEXT NOT NULL,
                           start_date TEXT,
                           end_date TEXT,
                           expected_end_date TEXT,
                           calender_event_id TEXT
                           )''')
        # Create session table
        connection.execute('''CREATE TABLE session
                           (_id INT AUTOINCREMENT NOT NULL,
                           session_id TEXT PRIMARY KEY NOT NULL,
                           carrier TEXT
                           )''')
        # Create carrier table
        connection.execute('''CREATE TABLE carrier
                           (_id INT AUTOINCREMENT NOT NULL,
                           created_at TEXT NOT NULL,
                           carrier_name TEXT PRIMARY KEY
                           )''')
        # Create affected_carrier table
        connection.execute('''CREATE TABLE affected_carrier
                           (_id INT AUTOINCREMENT PRIMARY KEY NOT NULL,
                            FOREIGN KEY(carrier_id) REFERENCES carrier(_id),
                            FOREIGN KEY(notification_id) REFERENCES notification(_id)
                           )''')
        # TODO: Create Relationships
        connection.execute("ALTER TABLE... ")
except connection.Error as e:
    print("Error {}:").format(e.args[0])
    sys.exit(1)

connection.close()
