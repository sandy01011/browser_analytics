#environment file
import json
import os
import subprocess


# google chrome target data, take user choice for data source
data_source = ['google_export_folder', 'google_chrome_folder'] # ge and gc
print('Please select target data type to be used i.e. gc for google chrome live data path\
       and ge for google exported data file, Press Enter to have both')

target_data = input("Enter gc or ge, return for both: ") or data_source

#user data

default_user = 'bran'
user = input('Enter user name: ') or default_user
user = 'sandeep'
default_profile = 'Default'
default_gc_path = '~/.config/google-chrome/'
default_brid = 'bran@dummy.com'
brid = input('Enter browsing id: ') or default_brid
gc_profiles = []
ops_ge_path = '../browser_analytics/raw_data/ge/'
ops_gc_path = '../browser_analytics/raw_data/gc/'
arc_gc_path = '../browser_analytics/archive_data/gc/'
arc_ge_path = '../browser_analytics/archive_data/ge/'
ge_ops_path = input('Enter ge path to read files: ') or ops_ge_path
gc_ops_path = input('Enter ge path to read files: ') or ops_gc_path
ge_arc_path = input('Enter ge path to read files: ') or arc_ge_path
gc_arc_path = input('Enter ge path to read files: ') or arc_gc_path

# profiles
check_profile = input('Do you want to load all profiles(Y/N): ') or 'Y'
if check_profile == 'Y':
    profiles_x = subprocess.check_output("find ~/.config/google-chrome/ -name 'Profile*'", shell=True)
    profiles_y = profiles_x.decode().splitlines()
    for profile in profiles_y:
        gc_profiles.append(profile)
    if os.path.exists(default_gc_path + default_profile):
        gc_profiles.insert(0, default_gc_path + default_profile)
    else:
        pass
else:
    gc_profiles = [default_profile]

# google chrome target data, take user choice for data source
data_source = ['google_export_folder', 'google_chrome_folder'] # ge and gc
print('Please select target data type to be used i.e. gc for google chrome live data path\
       and ge for google exported data file, Press Enter to have both')

target_data = input("Enter gc or ge, return for both: ") or data_source

#dataset list

data_list = ['History', 'Login Data']

user_init = {'user':brid, 'data':{'ge':{'ops_path':ge_ops_path,'arc_path':ge_arc_path},
                                  'ge':{'ops_path':gc_ops_path,'arc_path':gc_arc_path, 'profiles':gc_profiles, 
                                         'gc_data':data_list}
                                         }}

# mongo db data
db_user = 'whiteeye'
db_password = 'F0cus@p0int'
URI = "mongodb://aumnix.com:5017"
collectiondb = 'bran'
collection = 'branCollector'

db_init = {'dbuser':db_user,'dbpassword':db_password,'uri':URI, 'collectiondb':collectiondb, 'collection':collection}

# logger data
log_file = '../browser_analytics/logs/bd_main.log'
logger_name = 'bran_main'
log_handler = 'bran'

log_init = {'logfile':log_file, 'loggername':logger_name, 'loghandler':log_handler}

bran_init = {'user':user_init, 'db':db_init, 'logger':log_init}

def read_env():
    print('loading metadata')
    print(type(bran_init))
    return json.dumps(bran_init)








"""
bluemoon_profile = []

phone_profile = []
stl_profile = ['Profile4','Profile5','Profile6']
stl_profile_id = ['sandeepkumar.mishra@stl.tech', 'sk2011mishra@gmail.com', 'vigyan.netra@gmail.com']
history = 'History'
login = 'Login Data'
hist_list = []
login_list = []
# build path list for bluemoon and phone
for profile_curr in stl_profile:
    hist_list.append(data_path[0][0] + '/' + profile_curr + '/' + history)
    login_list.append(data_path[0][0] + '/' + profile_curr + '/' + login)
    browser_id = stl_profile
   # print(data_path[0][2])
   # print(profile)
   # print(history)

path_list = [hist_list, login_list, browser_id]

    



user_init = {'user':user, 'data_path':path_list}
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
"""