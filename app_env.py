#environment file
import json

#user data
user = 'sandeep'
browser_id = ['sk2011mishra@gmail.com'] # browser node id

data_path = [['/home/sandeep/anaconda3/envs/vconSanAI/jupyter_lab/github_sandy01011/browser_analytics/raw_data/sandeep/bluemoon','/home/sandeep/anaconda3/envs/vconSanAI/jupyter_lab/github_sandy01011/browser_analytics/raw_data/sandeep/phone','/home/sandeep/anaconda3/envs/vconSanAI/jupyter_lab/github_sandy01011/browser_analytics/raw_data/sandeep/stl_ubuntu']]
profile = ['Profile1','Profile2','Profile3']
history = 'History'
login = 'Login Data'
hist_list = []
login_list = []

for profile_curr in profile:
    hist_list.append(data_path[0][2] + '/' + profile_curr + '/' + history)
    login_list.append(data_path[0][2] + '/' + profile_curr + '/' + login)
   # print(data_path[0][2])
   # print(profile)
   # print(history)
path_list = [hist_list, login_list]

    



user_init = {'user':user, 'browser_id':browser_id, 'data_path':path_list}
# mongo db data
db_user = 'whiteeye'
db_password = 'F0cus@p0int'
URI = "mongodb://127.0.0.1:8017"
collectiondb = 'browsermon'
collection = 'browserCollector'

db_init = {'dbuser':db_user,'dbpassword':db_password,'uri':URI, 'collectiondb':collectiondb, 'collection':collection}

# logger data
log_file = '../logs/bd_main.log'
logger_name = 'bdmain'
log_handler = 'BD'

log_init = {'logfile':log_file, 'loggername':logger_name, 'loghandler':log_handler}

app_init = {'user':user_init, 'db':db_init, 'logger':log_init}

def read_env():
    print('loading meta')
    return json.dumps(app_init)

