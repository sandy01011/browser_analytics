import gridfs
import pymongo
import json
import sys
from app_env import read_env

metadata = json.loads(read_env())
db = metadata['db']['collectiondb']
db_collection = metadata['db']['collection']

class MongoDB(object):
    metadata = json.loads(read_env())
    username = metadata['db']['dbuser']
    password = metadata['db']['dbpassword']
    URI = metadata['db']['uri']
    db = metadata['db']['collectiondb']
    db_collection = metadata['db']['collection']
    DATABASE = None
    print(username, password, URI, db, db_collection)


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

    @staticmethod
    def gfs(collection, data):
        try:
            return gridfs.GridFS(MongoDB.DATABASE[collection].put(data))
        except Exception as e:
             print("An exception occurred ::", e)




def load_browser_data(mondb,data):
    MongoDB.initialize(db)
    #print('current db is {} collection is {}'.format(db, db_collection))
    try:
        MongoDB.insert(collection=db_collection,data=data)
    except Exception:
        print('load_bot_meta_to_db error occured')


