# This file will have browsing data parser class
import sqlite3
import json
from pandas import DataFrame
from mongo_loader import load_browser_data
import datetime
from applogger import BotLog



class BdParser(object):
    def __init__(self):
        #self.env = env_json
        #self.user = {}
        #self.db = {}
        #self.log = {}
        pass



    def load_env(self):
        #env = json.loads(self.env_json)
        pass


    def pre_parser(self, history, login, browser_id):
        if len(history) > 0 and len(login) > 0:
            for bid in range(len(history)):
                history1 = sqlite3.connect(history[bid])
                login1= sqlite3.connect(login[bid])
                brow_id = browser_id[bid]
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
                browsing_data = {'bid': brow_id, 'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'data': {'search': json.loads(df_h1_search.T.to_json()),'history': json.loads(df_h1.T.to_json()),'login': json.loads(df_l1.T.to_json()), 'downloads': json.loads(df_h1_downloads.T.to_json())}}
                try:
                    load_browser_data('collection',browsing_data)
                except error as e:
                    print(e)
                #print(browsing_data)

        else:
            print("meta data issue")


    def raw_parser(self):
        pass
