import sqlite3
import pandas as pd

def run_query(query):
    return pd.read_sql_query(query, db)

# connect db
db = sqlite3.connect('test2024.db')
cursor = db.cursor()

# 1
cursor.execute('''
DROP TABLE COMPANY
''')
# create db
cursor.execute('''
CREATE TABLE COMPANY
       (Store_ID CHAR(50),
       Salesperson CHAR(50),
       Sales INT
       );
       
''')
db.commit()

# 2
cursor.execute("INSERT INTO COMPANY (Store_ID,Salesperson,Sales) \
      VALUES ('1', 'Aaron' , 374  )")
db.commit()

q = ''' select * from COMPANY; '''
run_query(q)