# start browser data collection
import json
from bran_meta import read_env
from bran_collector import BranCollector
import bran_collector as bc
env = read_env()
metadata = json.loads(env)

# Collect data from source folder load it to db and create collector Json file
# put folder sensor to collect files
BranCollector(metadata).chrome_file()

# # check collectors allocated to bran
# print(bran_env[''])

# # call pre-parser to get json
# bdparser = BdParser()
# history_list = bran_env['user']['data'][0]
# login_list = bran_env['user']['data'][1]
# browser_id_list = bran_env['user']['data'][2]
# bdparser.pre_parser(history_list, login_list, browser_id_list)
# # enrich json

# # create json file

# # load to mongo db
# # archive data

