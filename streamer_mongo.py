from pymongo import MongoClient
import gridfs
import threading


try:
    #connect to DB
    client = MongoClient('localhost', 27017)
    fs = gridfs.GridFS(client.testGridFS)
except Exception as e:
    print(e)


def printit():
    threading.Timer(5.0, printit).start()
    #add date and take last 12
    fs.find({}).sort('date', -1)


printit()
