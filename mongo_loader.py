import gridfs
import pymongo
import json
import sys
from app_meta import meta


metadata= meta()
db = metadata[3]
db_collection = metadata[4]

class MongoDB(object):
    metadata = meta()
    username = metadata[0]
    password = metadata[1]
    URI = metadata[2]
    db = metadata[3]
    db_collection = metadata[4]
    DATABASE = None


    @staticmethod
    def initialize(db):
        try:
            client = pymongo.MongoClient(MongoDB.URI)
            MongoDB.DATABASE = client[MongoDB.db]
            MongoDB.DATABASE.authenticate(MongoDB.username, MongoDB.password)
            #print('db initialized')
        except Exception:
            print("Fatal error in main loop")

    @staticmethod
    def insert(collection, data):
        try:
            #for k,v in data.items():
            #    print(k, v)
            MongoDB.DATABASE[collection].insert(data, check_keys=False)
        except Exception as e:
             print("An exception occurred ::", e)

    @staticmethod
    def insertmany(collection, data):
        MongoDB.DATABASE[collection].insert(data)



def load_browser_data(mondb,data):
    MongoDB.initialize(db)
    #print('current db is {} collection is {}'.format(db, db_collection))
    try:
        MongoDB.insert(collection=db_collection,data=data)
    except Exception:
        print('load_bot_meta_to_db error occured')


