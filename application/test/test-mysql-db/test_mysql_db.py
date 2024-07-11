import sys
sys.path.append( './../../inc' )
sys.path.append( './../../src' )

import config
import db as DB

def test_db_connection():
    print('Testing  db_init() function')
    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)
    if( status == 'OK'):
        print("PASS");


def test_db_create_database(db_name):
    print('Testing  db_create_database()')
    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)
    print(db_name)
    if( status == 'OK'):
        DB.db_create_database(db_name)
        db_list = DB.db_show_databases()
        print('Recieved list = ',db_list)
        for i in db_list:
            print('ITEM')
            print(i)
            if ( db_name in i):
                print( 'DB Created Success , PASS')
                break;

def test_db_drop_database(db_name):
    print('Testing  db_drop_database()')
    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)
    print(db_name)
    if( status == 'OK'): 
        db_list = DB.db_show_databases()
        for i in db_list:
            #print(i)
            if ( db_name in i):
                DB.db_drop_database(db_name)
                break;
        db_list = DB.db_show_databases()
        found = False
        for i in db_list:
            #print(i)
            if ( db_name in i):
                print( 'DB Found ')
                found = True
                break;
    if found == True:
        print('FAIL')
    else :
        print('PASS')




if __name__ == '__main__':
    testcase_id  = int(sys.argv[1])

    for p in sys.path:
        print('PATH  = ',p)

    print('TEST CASE ID  = ',testcase_id)

    if(testcase_id == 1):
        test_db_connection()

    elif (testcase_id == 2):
       print('DB NAME = ', sys.argv[2])
       test_db_create_database(sys.argv[2])
            

    elif(testcase_id == 3):
        print('DB NAME = ', sys.argv[2])
        test_db_drop_database(sys.argv[2])



   