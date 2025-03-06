from Authentication import cursor , db
from Data_Extract import file

create_table_query = """
CREATE TABLE IF NOT EXISTS users(
id int,
name varchar(100),
username varchar(100),
email varchar(100),
address varchar(100),
phone varchar(100),
website	varchar(100),
company varchar(100)
);
"""

cursor.execute(create_table_query)
db.commit()


# SQL Query to insert data
insert_query = "INSERT INTO users (id,name,username, email, phone,website) VALUES (%s, %s, %s, %s, %s, %s)"

# Insert data into MySQL
for user in file:
    cursor.execute(insert_query, (user["id"],user["name"],user["username"], user["email"],user["phone"],user["website"]))

db.commit()  # Commit changes
print(f"{cursor.rowcount} records inserted successfully.")

# Close the connection
cursor.close()
db.close()