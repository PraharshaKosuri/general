import socket
import sys
import threading
import time

import data_process as PROCESS

client_list = []

def client_tx():
    print("Starting server thread ")
    while True:
        i = 0
        for i in range(len(client_list)):
            client = client_list[i]
            conn = client["client_handle"]
            print("Give Message To Client=", client["client_addr"])
            message = input(f'Enter your message for client -> ')
            conn.send(message.encode('utf-8'))

def client_rx():
    print("Starting client_rx thread")
    while True:
        for client in client_list:
            conn = client["client_handle"]
            addr = client["client_addr"]
            data = conn.recv(1024)
            if data:
                    print(f"Received message from {addr}: {data.decode('utf-8')}")
                    message = data.decode('utf-8')
                    PROCESS.data_process_rx(client["client_handle"],message)
                              

def server_program(ip, port):
    print('server ip = ',ip)
    print('server port = ',port)
    is_thread_started = False
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, int(port)))
    server_socket.listen()
    print(f"Server listening on {ip}:{port}")
    while True:
        conn, address = server_socket.accept()
        client_dict = {"client_handle": conn, "client_addr": address}
        client_list.append(client_dict)

        if not is_thread_started:
            print("Starting Threads")

            client_tx_h = threading.Thread(target=client_tx, args=())
            client_tx_h.start()

            client_rx_h = threading.Thread(target=client_rx, args=())
            client_rx_h.start()

            is_thread_started = True

    server_socket.close()