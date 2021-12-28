# start browser data collection
import json
from bd_parser import BdParser
from app_env import read_env

# load environement and logger
bd_env = json.loads(read_env())
#bd_agent_load_env = bd_agent_read_env.load_env()
#bd_agent = bd_agent
#print(bd_env)


# call pre-parser to get json
#print(len(bd_env['user']['data_path'][1]))
bdparser = BdParser()
history_list = bd_env['user']['data_path'][0]
login_list = bd_env['user']['data_path'][1]
browser_id_list = bd_env['user']['data_path'][2]
bdparser.pre_parser(history_list, login_list, browser_id_list)
# enrich json

# create json file

# load to mongo db


