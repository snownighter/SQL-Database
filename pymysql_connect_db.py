import pymysql as mysql

try:
    # connect
    conn = mysql.connect(
        host='localhost',
        port=3306, user='root',
        password='57319',
        database='mysql2024'
    )
    with conn.cursor() as cursor:

        cursor.execute('''
        INSERT INTO `app_info` (name) VALUES ('insert_python');
        ''')

        cursor.execute('SELECT * FROM `app_info`;')
        records = cursor.fetchall()

        for r in records:
            print(r)

    #conn.commit()

    # free
    conn.close()

except Exception as ex:
    print(ex)

