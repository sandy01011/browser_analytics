# This file will collect data from google chrome live file,gc and from google export
# This file will load data to mongodb and will create a file on disk

import sqlite3
import json
from pandas import DataFrame
from bran_meta import read_env
from mongo_loader import load_browser_data
import datetime
from applogger import BotLog

metadata = json.loads(read_env())
logger = BotLog(metadata['logger']['logfile'], metadata['logger']['loggername'], metadata['logger']['loghandler']).get_logger()
logger.info('bran env loaded')

class BranCollector:
    def __init__(self):
        self.user = metadata['user']['user']
        self.db_user = metadata['db']['dbuser']
        self.db_pass = metadata['db']['dbpassword']
        self.db_uri = metadata['db']['uri']
        self.db_collectiondb = metadata['db']['collectiondb']
        self.db_collection = metadata['db']['collection']
        self.ge_ops_path = metadata['user']['data']['ge']['ops_path']
        self.ge_arc_path = metadata['user']['data']['ge']['arc_path']
        self.gc_ops_path = metadata['user']['data']['gc']['ops_path']
        self.gc_arc_path = metadata['user']['data']['gc']['arc_path']
        self.gc_profiles = metadata['user']['data']['gc']['profiles']
        self.gc_data_hist = metadata['user']['data']['gc']['gc_data'][0]
        self.gc_data_login = metadata['user']['data']['gc']['gc_data'][1]
        self.history = ''
        self.login = ''
    

        
        print(self.user, self.db_user, self.db_pass, self.db_uri, self.gc_profiles,self.gc_data_hist)
        
"""
    def chrome_file(self):
        os.chdir(os.path.expanduser("~"))
        #bids = metadata[5]  # load browsing id's
        #history = metadata[6] # load history data
        #login = metadata[7]   # load login data
        #if len(self.users) > 0 and len(history) > 0 and len(login) > 0: # for multiple profiles
        if len(self.user) > 0:
            for bid in bids:
                history1 = sqlite3.connect(history[0])
                login1 = sqlite3.connect(login[0])
                h1 = history1.cursor()
                l1 = login1.cursor()
                h1.execute("SELECT urls.id id, urls.url url, urls.title title, urls.visit_count visit_count, urls.typed_count typed_count, urls.last_visit_time last_visit_time, urls.hidden hidden, visits.visit_time visit_time, visits.from_visit from_visit, visits.visit_duration visit_duration, visits.transition transition, visit_source.source source FROM urls JOIN visits ON urls.id = visits.url LEFT JOIN visit_source ON visits.id = visit_source.id")
                l1.execute("SELECT logins.username_value username, logins.username_element element, logins.origin_url origin,logins.action_url action, logins.date_created created_on, logins.date_last_used last_used from logins")
                h1_data = h1.fetchall()
                l1_data = l1.fetchall()
                # adding search keywords
                h1.execute("select * from keyword_search_terms")
                h1_search = h1.fetchall()
                # adding downloads
                h1.execute("select * from downloads")
                h1_downloads = h1.fetchall()
                # creating the dataframes
                df_h1 = DataFrame(h1_data,columns=["id", "url", "title", "visit_count", "typed_count", "last_visit_time", "hidden", "visit_time","from_visit", "visit_duration","transition", "source"])
                df_h1['last_visit_time'] = df_h1['last_visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
                df_h1['visit_time'] = df_h1['visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
                df_h1_search = DataFrame(h1_search, columns=["keyword_id", "url_id","term", "nterm"])
                df_h1_downloads = DataFrame(h1_downloads, columns=["id", "guid","current_path", "target_path","start_time", "received_bytes","total_bytes", "state","danger_type","interupt_reason","hash","end_time","opened", "last_access_time","transient", "referrer","site_url","tab_url", "tab_referrer_url","http_method", "by_ext_id","by_ext_name","etag","last_modified","mime_type", "original_mime_type"])
                df_l1 = DataFrame(l1_data,columns=["username", "element", "origin", "action", "created_on", "last_used"])
                df_l1['created_on'] = df_l1['created_on'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
                df_l1['last_used'] = df_l1['last_used'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
                h1.close()
                l1.close()
                browsing_data = {'bid': bid, 'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'data': {'search': json.loads(df_h1_search.T.to_json()),'history': json.loads(df_h1.T.to_json()),'login': json.loads(df_l1.T.to_json()), 'downloads': json.loads(df_h1_downloads.T.to_json())}}
                #load_browser_data('collection',browsing_data)
                print(browsing_data)

        else:
            print("meta data issue")
    
    def chrome_export():
        pass



history1 = sqlite3.connect('/home/sandeep/snap/chromium/common/chromium/Profile 4/History')
login1= sqlite3.connect('/home/sandeep/snap/chromium/common/chromium/Profile 4/Login Data')
h1 = history1.cursor()
l1 = login1.cursor()
h1.execute("SELECT urls.id id, urls.url url, urls.title title, urls.visit_count visit_count, urls.typed_count typed_count, urls.last_visit_time last_visit_time, urls.hidden hidden, visits.visit_time visit_time, visits.from_visit from_visit, visits.visit_duration visit_duration, visits.transition transition, visit_source.source source FROM urls JOIN visits ON urls.id = visits.url LEFT JOIN visit_source ON visits.id = visit_source.id")
l1.execute("SELECT logins.username_value username, logins.username_element element, logins.origin_url origin,logins.action_url action, logins.date_created created_on, logins.date_last_used last_used from logins")
h1_data = h1.fetchall()
l1_data = l1.fetchall()
# adding search keywords 
h1.execute("select * from keyword_search_terms")
h1_search = h1.fetchall()
# adding downloads
h1.execute("select * from downloads")
h1_downloads = h1.fetchall()
# creating the dataframes
df_h1 = DataFrame(h1_data,columns=["id", "url", "title", "visit_count", "typed_count", "last_visit_time", "hidden", "visit_time","from_visit", "visit_duration","transition", "source"])
df_h1['last_visit_time'] = df_h1['last_visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
df_h1['visit_time'] = df_h1['visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
df_h1_search = DataFrame(h1_search, columns=["keyword_id", "url_id","term", "nterm"])
df_h1_downloads = DataFrame(h1_downloads, columns=["id", "guid","current_path", "target_path","start_time", "received_bytes","total_bytes", "state","danger_type", 
                                                                      "interupt_reason","hash","end_time","opened", "last_access_time","transient", "referrer", 
                                                                      "site_url","tab_url", "tab_referrer_url","http_method", "by_ext_id","by_ext_name","etag",
                                                                      "last_modified","mime_type", "original_mime_type"])
df_l1 = DataFrame(l1_data,columns=["username", "element", "origin", "action", "created_on", "last_used"])
df_l1['created_on'] = df_l1['created_on'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
df_l1['last_used'] = df_l1['last_used'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
h1.close()
l1.close()
browsing_data = {'bid': bid, 'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
                 'data': {'search': json.loads(df_h1_search.T.to_json()),'history': json.loads(df_h1.T.to_json()), 
                           'login': json.loads(df_l1.T.to_json()), 'downloads': json.loads(df_h1_downloads.T.to_json())}}
load_browser_data('collection',browsing_data)
"""
