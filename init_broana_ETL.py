# start browser data collection
import json
from bd_parser import BdParser
from bran_env import read_env

# load environement and logger
baake_env = json.loads(read_env())

# call pre-parser to get json
bdparser = BdParser()
history_list = baake_env['user']['data'][0]
login_list = baake_env['user']['data'][1]
browser_id_list = baake_env['user']['data'][2]
bdparser.pre_parser(history_list, login_list, browser_id_list)
# enrich json

# create json file

# load to mongo db


