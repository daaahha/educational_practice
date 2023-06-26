import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor 
    )
    print('Всё гуд')

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM Users')
            USERS = cursor.fetchall()
            print(USERS)
    finally:
        connection.close()

except Exception as ex:
    print(ex)



# Обращаешься к этому URL
# http://158.160.105.229:5000/logs?ip={Entry.ip}&start_date={Entry.DataStart}&end_date={Entry.DataEnd}
# Где IP- фильтр по IP
# Start_date и end date-От какой даты до какой идет фильтрация