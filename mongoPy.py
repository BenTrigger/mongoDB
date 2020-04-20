from pymongo import MongoClient
from event import Event
import pickle
import bson
from bson.objectid import ObjectId
import gridfs
import datetime
import sys


try:
    #connect to DB
    client = MongoClient('localhost', 27017)
    db = client.test
    collectinT = db.events

    db2 = client.testGridFS
    fs = gridfs.GridFS(db2)



    #insert An Events
    # for i in range(4):
    #     collectinT.insert_one(Event().set__file_path(file_name="ben").__dict__)

    #Find events from DB by data time
    # from_date = datetime.datetime(2010, 12, 31, 12, 30, 30, 125000)
    # to_date = datetime.datetime(2020, 12, 31, 12, 30, 30, 125000)
    # for event in collectinT.find({"created_date": {"$gte": from_date, "$lt": to_date}}):
    #     print(event['created_date'])

    #write/read pickle to D
    #pickle.dump(mosi['test']['audio'][0], open("audio_0.pkl", "wb"))
    data = pickle.load(open("mosi_data.pkl", "rb"))
    #data = pickle.load(open("audio.pkl", "rb"))
    thebytes = pickle.dumps(data)  # size in bytes 1372196

    if sys.getsizeof(thebytes) >= 16793598:  #max byte size
        #fs.put(fs.get(a), filename="foo", bar="baz")
        file_id = fs.put(thebytes, filename="source_file_name_here",bar="status_new")
        #print(pickle.loads(fs.get(file_id).read()))
        exit(1)
    else:
        event = Event().add_bin_file(thebytes)
        ins_id = collectinT.insert_one(event.__dict__).inserted_id
        print(ins_id)

    #GET THE FILE FROM MONGO
    items = collectinT.find({'_id': ins_id})
    for item in items:
        for bina in item['bin_files']:
            pickle_from_bytes = pickle.loads(bina)
            print(pickle_from_bytes)

    print("Done")
except Exception as e:
    print(e)





