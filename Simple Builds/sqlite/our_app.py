import main 

# add a record to the database
main.add_one("Laura","Smith","laura@smith.com")

# Delete Record use rowid as string
main.delete_one('10')

# Add many records
stuff = [
    ('Brend', 'Smithy', 'breth@gmail.com',),
    ('Josh', 'Raintree', 'josh@gmail.com',)
]

# main.add_many(stuff)

main.where_id("11")


# show all records
main.show_all()

