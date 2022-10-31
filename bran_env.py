#environment file for bran engine
import json

#user data
user = 'sandeep' # get user name from form input
 # browser node id static manual mapping with profile index based list map
browser_id = ['sk2011mishra@gmail.com']
# take user choice for data source
data_source = ['google_export_folder', 'google_chrome_folder']
# get data path from user form input
data_path = '/home/sandeep/anaconda3/envs/vconSanAI/jupyter_lab/github_sandy01011/browser_analytics/raw_data/sandeep/bluemoon/bluemoon-sk2011mishra-gmail_com_n-1/'
history = [data_path + 'History']
login = [data_path + 'Login Data']
user_init = {'user':user, 'data':[history, login, browser_id]}
# mongo db data
db_user = 'whiteeye'
db_password = 'F0cus@p0int'
URI = "mongodb://aumnix.com:5017"
collectiondb = 'bran'
collection = 'branCollector'

db_init = {'dbuser':db_user,'dbpassword':db_password,'uri':URI, 'collectiondb':collectiondb, 'collection':collection}

# logger data
log_file = '../logs/bd_main.log'
logger_name = 'bran_main'
log_handler = 'bran'

log_init = {'logfile':log_file, 'loggername':logger_name, 'loghandler':log_handler}

bran_init = {'user':user_init, 'db':db_init, 'logger':log_init}

def read_env():
    print('loading meta')
    return json.dumps(bran_init)

