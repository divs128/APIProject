import mysql.connector

"""
This file contains the necessary code for establishing a connection to the MySQL database 
and provides a cursor object for executing SQL queries
"""

# Establish database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Emids123',
    database='python_flask'
)

# Create a cursor object
cursor = conn.cursor()
cursor.execute("SELECT * FROM user")
result = cursor.fetchall()
print(result)