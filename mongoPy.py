from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.test
collectinT = db.people

for val in collectinT.find({}):
    print(val['firstname'])

