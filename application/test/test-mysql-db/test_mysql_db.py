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

def test_db_create_table(db_name , table_name):    
    print('Testing  db_create_table()')

    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)
    DB.db_create_database(db_name)

    column_count=2
    column_list=[]
    c={"column_name":"Id ",
       "column_data_type":"INT"}
    column_list.append(c)
    c={"column_name":"Name",
       "column_data_type":"VARCHAR(20)"} #VARCHAR is character array type for sql 20 indicates length of array
    column_list.append(c)



    DB.db_create_table(db_name,table_name,column_count,column_list)
    result = DB.db_is_table_present(db_name , table_name)
    if ( result == 'OK'):
        print('PASS')
    else:
        print('FAIL')



def test_db_create_table_entry(db_name , table_name):  
 
    print('Testing  db_create_table_entry()')
    test_db_create_table(db_name , table_name)
    #status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)
    column_count=2
    column_list=[]
    c={"column_name":"Id ",
       "value":2}
    column_list.append(c)
    c={"column_name":"Name",
       "value":"prahi2"} 
    column_list.append(c)

    DB.db_create_table_entry(db_name,table_name,column_count,column_list)



def test_db_get_full_entry(db_name , table_name,col_name,col_value):  
 
    print('Testing  db_get_full_entry()')
    status, c1 = DB.db_init(config.database_ip,config.database_port,config.database_userid,config.database_password)

    entry_list=DB.db_get_full_entry(db_name,table_name,col_name,col_value)
    for i in range(len(entry_list)):
        print(entry_list[i])



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

    elif(testcase_id == 4):
        test_db_create_table(sys.argv[2] , sys.argv[3])

    elif(testcase_id == 5):
        test_db_create_table_entry(sys.argv[2] , sys.argv[3])

    elif(testcase_id == 6):
        test_db_get_full_entry(sys.argv[2] , sys.argv[3] , sys.argv[4] , sys.argv[5])

    




   