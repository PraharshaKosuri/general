import sys
import mysql.connector


db_conn = None

 
#####   Data Base Connection  ####        
def db_init(db_host, db_port, db_user, db_password):
    global db_conn
    status = 'OK' 
    if db_conn is None or not db_conn.is_connected():
            db_conn = mysql.connector.connect(
                host=db_host,
                port=db_port,
                user=db_user,
                password=db_password
            )
            print("Connected to mysql")            
    else:
        print("Database connection is already active")
        status = 'NOT OK' 

    return status, db_conn


#### Database  Functionality ####
def db_create_database(db_name):
    query="CREATE DATABASE IF NOT EXISTS  "+ db_name
    print(query)
    db_conn.cursor().execute(query)

def db_drop_database(db_name):
    query="DROP DATABASE "+ db_name
    print(query)
    db_conn.cursor().execute(query)

def db_show_databases():
    db_list=[]
    query="SHOW DATABASES"
    print(query)
    #result = db_conn.cursor().execute(query)
    with db_conn.cursor() as cursor:
        cursor.execute(query)
        for db in cursor:
            db_list.append(db)
            print(db)
    print(db_list)
    return db_list

def db_use_database(db_name):
    query="USE  "+ db_name
    print(query)
    db_conn.cursor().execute(query)

#create table abc (field1 int,field2 int);

def db_create_table(db_name,table_name,column_count,column_list):
      
    print("db_create_table() Entry")
 
    ### Argument checking 
    for i in range (column_count):
        t=column_list[i]
        print(t["column_name"])
        print(t["column_data_type"])
    db_use_database(db_name)

    ### Query preparation 
    query="CREATE TABLE IF NOT EXISTS " + table_name + "  ("
    
    for i in range (column_count):
        t=column_list[i]
        query=query + t["column_name"]
        query=query +  " " + t["column_data_type"] 
        if( i != column_count -1):
            query = query + " , "
    query = query + " ) "
    print(query)

    ### Query Execution
    db_conn.cursor().execute(query)

def db_is_table_present(db_name , table_name):
    db_use_database(db_name)
    query="SHOW TABLES"
    print(query)
    with db_conn.cursor() as cursor:
        cursor.execute(query)
        for item in cursor:
            print(item)
            if (table_name  in item):
                print( 'Table Found ')
                return 'OK'
                break; 
    return 'NOT_OK'



