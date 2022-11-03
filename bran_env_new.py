#environment file
import json
import os
import subprocess


#user data

default_user = 'bran'
user = input('Enter user name: ') or default_user
user = 'sandeep'
default_profile = 'Default'
default_data_path = '~/.config/google-chrome/'
default_brid = 'bran@dummy.com'
brid = input('Enter browsing id: ') or default_brid

# profiles
check_profile = input('Do you want to load all profiles(Y/N): ') or 'Y'
if check_profile == 'Y':
    profiles_x = subprocess.check_output("find ~/.config/google-chrome/ -name 'Profile*'", shell=True)
    profiles = []
    profiles_y = profiles_x.decode().splitlines()
    for profile in profiles_y:
        profiles.append(profile)
    if os.path.exists(default_data_path + default_profile):
        profiles.insert(0, default_data_path + default_profile)
    else:
        pass
    #profiles = profiles_y.insert(1,default_data_path + default_profile)
    print(profiles)
else:
    profiles = [default_profile]
    

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