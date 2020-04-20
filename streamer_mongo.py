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

from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.start()

def some_job():
    print "Every 10 seconds"

sched.add_interval_job(some_job, seconds = 10)

....
sched.shutdown()