import json
import socket
import sys
import threading
import time


def data_process_rx(conn , message):
    print(message)
    conn.send("Received ")
    
    

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:
#print(y["age"])