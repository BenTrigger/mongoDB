from pymongo import MongoClient
from event import Event
import pickle
import bson
#import datetime

#connect to DB
client = MongoClient('localhost', 27017)
db = client.test
collectinT = db.events

#insert An Events
for i in range(4):
    collectinT.insert_one(Event().set__file_path(file_name="ben").__dict__)

#Find events from DB by data time
# from_date = datetime.datetime(2010, 12, 31, 12, 30, 30, 125000)
# to_date = datetime.datetime(2020, 12, 31, 12, 30, 30, 125000)
# for event in collectinT.find({"created_date": {"$gte": from_date, "$lt": to_date}}):
#     print(event['created_date'])

#write pickle to DB
mosi = pickle.load( open( "mosi_data.pkl", "rb" ) )

bins_coll = db.bins
thebytes = pickle.dumps(mosi)
bins_coll.insert({'bin-data': bson.Binary(mosi)})

