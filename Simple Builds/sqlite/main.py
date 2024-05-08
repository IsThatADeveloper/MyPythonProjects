import sqlite3
import os

# # conn = conn = sqlite3.connect(':memory:') # deletes once youre done, not permanent
# conn = sqlite3.connect('customer.db')

# # cd /Users/Eshaan/OneDrive/Documents/Code/sqlite # Pathway
# # python main.py # To run

# # Create a cursor
# c = conn.cursor()


# QUERY The DATABASE AND RETURN ALL RECORDS
def show_all():

    conn = sqlite3.connect('customer.db')
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()

    for item in items: 
        print(item)

    conn.commit()
    conn.close()

# ADD A RECORD FUNCTION (NEW RECORD TO TABLE)
def add_one(first,last,email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()

# ADD MANY TO LIST TABLE
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))

    conn.commit()
    conn.close()


# ADD A RECORD FUNCTION (NEW RECORD TO TABLE)
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", (id,))
    
    conn.commit()
    conn.close()

# WHERE CLAUSE ID
def where_id(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * from customers WHERE rowid = (?)", (id,))
    items = c.fetchall()

    for item in items: 
        print(item)
    
    conn.commit()
    conn.close()

# WHERE CLAUSE EMAIL
def where_id(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * from customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items: 
        print(item)
    
    conn.commit()
    conn.close()

# Update Records
# c.execute("""UPDATE customers SET first_name = 'Mary'
#           WHERE rowid = 1
# """)

# conn.commit()

# Delete Records
# c.execute("DELETE from customers WHERE rowid = 8")
# conn.commit()

# c.execute("SELECT rowid, * FROM customers") # star means all
# c.execute("SELECT * FROM customers WHERE last_name = 'Brown'")
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'Br%'")
# c.execute("SELECT * FROM customers WHERE email LIKE '%gmail.com'")

# Ordering
# c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
# conn.commit()

# AND & OR
# c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Br%' OR rowid = 2")
# conn.commit()

# Limiting
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2")
# conn.commit()

# Delete table and backups
# c.execute("DROP TABLE customers") # CAREFUL USING IT 
# conn.commit()

# print(c.fetchone()[0])
# print(c.fetchmany(3))

# print("NAME " + "\t\tEMAIL")
# print("-----" + "\t\t--------")
# for item in items:
#     print(item[0] + "\t" + item[1] + "\t" + item[2])

# many_customers = [('Wes', 'Brown', 'wes@gmail.com'), 
#                   ('Mary', 'Brown', 'mary@gmail.com'), 
#                   ('Reed', 'White', 'white@gmail.com'),
#                   ]

# c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

# Create a Table
# c.execute("""CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
# )""")

# DATATYPES: Null, Integer: Number, Real: Decimal, Text, Blob: Pictures, movie, etc

# print("Command executed successfully...")

# # Commit our command
# conn.commit()

# # Close our connection
# conn.close()


