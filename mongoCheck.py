import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017) # MongoClient(username="user name", password="pass/word")
db = client.get_database('thepolyglotdeveloper')
collection = db.get_collection('people')

for var in collection.find({ "firstname": "Nic" }):
    print(var['firstname'])

#not safe it might not found an object:
print(collection.find_one({ "firstname": 'Nic' })['firstname'])

#If not exists creates a new collection
people = db.peoplesss
user = {
        "first_name": "ben",
        "last_name": "lerer",
    }
user_id = people.insert_one(user).inserted_id
print(user_id)
