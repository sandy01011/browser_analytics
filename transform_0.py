# This file will transform data
import pymongo
from bran_meta import read_env
#from mongo_loader import read_browser_data, update_layer
import json

metadata = json.loads(read_env())
db_col = metadata['db']['collectiondb']
db_collection = metadata['db']['collection']


#metadata = meta()
username = metadata['db']['dbuser']
password = metadata['db']['dbpassword']
URI = metadata['db']['uri']
# db_col = metadata[3]
# db_col_par = metadata[4]['ppONbids']
# db_col_col = metadata[4]['rawONbids']
client = pymongo.MongoClient(URI)
db = client[db_col]
db.authenticate(username, password)
collection = db[db_collection]
# parsing = db[db_col_par]
collection_list_0 = collection.find({'layer':0})
collection_list = [data for data in collection_list_0]
print(len(collection_list))


# read data
# data_list = read_browser_data()
# print(data_list)

# data cleaning, and composition
# remove dublicates

# EDA reports TimeSeries

# enrichment with doc_type (HTML,pdf,csv,vedio etc.) classfication and EDA enrichments
