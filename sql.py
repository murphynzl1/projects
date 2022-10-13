from pickle import TRUE
from secrets import choice
import mysql.connector
from mysql.connector import Error
c=[]
t=[]
q="" 

def con_db(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = con_db("localhost","nigel","zaq12wsx","project")

opt=input("What do want to do (Create, edit, insert, alter,show)? ")

match opt:
    case "create":
        table=input("What is the table name? ")
        
        while True:
            col=input("What is field name? ")
            type=input("What is the field type? ")
            c.append(col)
            t.append(type)
            
            if input("Add other one y/n? ") == "n":
                break
        
        for i in range(len(c)):
            q=q+c[i]+" , "=t[i]

print(q)

#execute_query(connection,q)