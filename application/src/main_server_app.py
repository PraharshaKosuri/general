import sys
sys.path.append( './../inc' )
sys.path.append( './../test' )

import config
import db as DB


import socket
import tcp_server as SERVER


if __name__ == '__main__':
    SERVER.server_program(config.server_ip,config.server_port)
    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)