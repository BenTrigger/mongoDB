from pymongo import MongoClient
from event import Event

import datetime

client = MongoClient('localhost', 27017)
db = client.test
collectinT = db.events


# eventShow = ({
#     'name': "example3",
#     'created_date': datetime.datetime.now()
# })
#
for i in range(4):
    collectinT.insert_one(Event().set__file_path(file_name="ben").__dict__)

# from_date = datetime.datetime(2010, 12, 31, 12, 30, 30, 125000)
# to_date = datetime.datetime(2020, 12, 31, 12, 30, 30, 125000)
# for event in collectinT.find({"created_date": {"$gte": from_date, "$lt": to_date}}):
#     print(event['created_date'])


# for val in collectinT.find({}):
#     print(val['firstname'])


