import socket
import sys
import threading
import time
import mysql.connector

client_list = []
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
    query="CREATE DATABASE "+ db_name
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