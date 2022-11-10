#import gridfs
import pymongo
import json
import sys
from bran_meta import read_env
from applogger import BotLog


metadata = json.loads(read_env())
db = metadata['db']['collectiondb']
db_collection = metadata['db']['collection']

logger_name = metadata['logger']['loggername']
logger_handler = metadata['logger']['loghandler']
logger_file = metadata['logger']['logfile']
logger = BotLog(logger_file, logger_name, logger_handler).get_logger()
logger.info('db env loaded')


class MongoDB(object):
    metadata = json.loads(read_env())
    username = metadata['db']['dbuser']
    password = metadata['db']['dbpassword']
    URI = metadata['db']['uri']
    db = metadata['db']['collectiondb']
    db_collection = metadata['db']['collection']
    DATABASE = None
    print('db name {}, user name {}, password {}, uri {}, collection {}'.format(db,username,password,URI, db_collection))

    @staticmethod
    def initialize(db):
        try:
            client = pymongo.MongoClient(MongoDB.URI)
            MongoDB.DATABASE = client[MongoDB.db]
            MongoDB.DATABASE.authenticate(MongoDB.username, MongoDB.password)
        except Exception as e:
            print("Fatal error in main loop", e)

    @staticmethod
    def insert(collection, data):
        try:
            MongoDB.DATABASE[collection].insert(data, check_keys=False)
            print('db name', collection)
        except Exception as e:
             print("An exception occurred during insert:", e)

    @staticmethod
    def insertmany(collection, data):
        try:
            MongoDB.DATABASE[collection].insert_many(data)
        except Exception as e:
             print("An exception occurred during insertmany :", e)


    # @staticmethod
    # def gfs(collection, data):
    #     try:
    #         return gridfs.GridFS(MongoDB.DATABASE[collection].put(data))
    #     except Exception as e:
    #          print("An exception occurred ::", e)




def load_browser_data(data):
    logger.info('load browser data started')
    MongoDB.initialize(db)
    try:
        MongoDB.insert(collection=db_collection,data=data)
        print(db_collection)
        logger.info('data loaded to db')
    except Exception as e:
        logger.error("load browser data exception occurred:", e)
        print('load_bot_meta_to_db error occured')


