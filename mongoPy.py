from pymongo import MongoClient

mongoC = MongoClient(host="localhost",port=27175)
db = mongoC.get_database("test")
collectinTemp = db.people
for var in collectinTemp:
    print(var)