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

# archive loaded files

