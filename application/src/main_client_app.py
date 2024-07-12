import sys
sys.path.append( './../inc' )
sys.path.append( './../test' )

import config
import db as DB


import socket
import tcp_client as CLIENT


if __name__ == '__main__':
    CLIENT.client_program(config.server_ip,config.server_port)