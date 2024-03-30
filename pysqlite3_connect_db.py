import sqlite3 as sql
import pandas as pd

# connect
conn = sql.connect('sqlite2024.db')

cursor = conn.cursor()
cursor.execute('''
INSERT INTO `app_info` (name) VALUES ('insert_python');
''')

#query = ''' SELECT * FROM `app_info`; '''
#pd.read_sql_query(query, conn)

# 有效更新
#conn.commit()
cursor.execute('SELECT * FROM `app_info`;')
records = cursor.fetchall()

for r in records:
    print(r)

# free
cursor.close()
conn.close()

"""
INSERT INTO app_info (name) VALUES ('insert_app2');
UPDATE app_info SET name='update_app', version='2.0' WHERE id=4;
DELETE FROM app_info WHERE name='insert_app2';
SELECT * FROM app_info WHERE date IS NULL;
"""
