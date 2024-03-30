from pymongo import MongoClient

db_name = 'mongo2024'
collection_name = 'app_info'

# connect
client = MongoClient("mongodb://localhost:27017/")
database = client[db_name]

print("DB  | ", client.list_database_names())

collection = database[collection_name]
'''
collection.insert_many([
    {'name':'test','vision':2.0},
    {'name':'create','vision':3.0}
])
'''
for record in collection.find():
    print(record)