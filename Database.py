#We will be connecting to the sql database
# import libraries
''' 
pip command to install MYSQL connector pyhton package is 
pip install mysql-connector-pyhton. Do this in the command line through the python package you are using
'''

import mysql.connector
from mysql.connector import Error
import pandas as pd

# write a user defined function that will enable a server connection
# the user defined function takes three parameters
# a variable is defined and assigned a value called none
# mysql.connector.connect creares a connection with the sql server 
def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password
        )
        print("MySQL Database connection successful")

    except Error as err:
        print(f"Error: '{err}""")
    return connection

#put our MySQL Terminal password which is the password that you use to open MySQL workbench
pw = "(Civil1engr2devops3)"

# Databse name will be the name of the database you wish to create
db = "MySQL_Python"

connection = create_server_connection("localhost", "root", pw)

# with this you will get an output "MySQL Database Connection successful"

# Now will craete a database called mysql_python
# to do this i will create another function
# MySQLs cursor of mysql connector python is used to execute statements to communicate to the mysql database
# Mysql cursor class initiates objects that can execute operations such as the mysql statements.

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as err:
        print(f"Error: '{err} '")

create_database_query = "Create database mysql_python"
create_database(connection, create_database_query)

# This will show an output " Database created successfully"

# Connect to database
# Now we are going to connect to the database that we just created.

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database =db_name
        )
        print("MySQL database connection successfull") 
    except Error as err:
        print(f"Error: '{err}'")
    return connection

# Execute SQL Queries
# lets execute some sql queries

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query was successfull")
    except Error as err:
        print(f"Error: '{err}'")

# Now lets create an sql query that is assigned to a variable create_orders_table.

create_orders_table = """
create table orders(
order_id int primary key,
customer_name varchar(30) not null,
product_name varchar(20) not null,
date_ordered date,
quantity int,
unit_price float,
phone_number varchar(20));
"""

# connect to the database and call the function excute_query that takes two arguments 

connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_orders_table)

# this creates a table in the sql server

#lets Insert data into the table we just created

data_orders = """
insert into orders values
(101, "steve", "laptop", "2018-06-12", 2, 800, "62937879"),
(102, "Jos", "Books", "2019-02-10", 10, 12, "56938974"),
(103, "stacy", "Trousers", "2019-12-25", 5, 50, "14350957"),
(104, "Nancy", "T-shirts", "2018-07-14", 7, 30, "09761893"),
(105, "Maria", "Headphones", "2019-05-30", 6, 48, "46730926"),
(106, "Danny", "Smart Tv", "2018-08-20", 10, 300, "29845604");
"""
connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, data_orders)

# Lets create another user defined function that reads queries and display the functions

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

# Using the select stmt
q1 = """
select * from orders;
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)
for result in results:
    print(result)

# lets write a query that displays specified columns
q2 = """
select customer_name, phone_number from orders;
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q2)
for result in results:
    print(result)

# to display the year in the date_ordered column
q3 = """
select year(date_ordered) from orders;
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q3)
for result in results:
    print(result)

# Using the where clause
q4 = """
select * from orders where date_ordered < "2018-12-31"
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q4)
for result in results:
    print(result)

# the orderby sorts your results based on aparticular column
q5 = """
select * from orders order by unit_price;
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q5)
for result in results:
    print(result)

# lets create a dataframe from the given table
'''
create an empty list from_db, create a for loop and append the result to from_db
result = list(result) puts the result in a list format
df = pd.DataFrame converts the lists to a dataframe
'''
from_db = []

for result in results:
    result = list(result)
    from_db.append(result)
columns = ["ordered_id", "customer_name", "product_name", "date_ordered", "quantity",
           "unit_price", "phone_number"]
df = pd.DataFrame(from_db, columns = columns)

print(df)

# Update Commamd: suppose you want to change the unit price of one of the orders
update = """
update orders 
set unit_price = 45
where order_id = 103;
"""
connection =create_db_connection("localhost", "root", pw, db)
execute_query(connection, update)

# Delete command
delete_order = """
delete from orders
where order_id = 105;
"""
connection =create_db_connection("localhost", "root", pw, db)
execute_query(connection, delete_order)

