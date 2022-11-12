# This file will collect data from google chrome live file,gc and from google export
# This file will load data to mongodb and will create a json file on disk

import os
import shutil
import sqlite3
import json
from pandas import DataFrame

from mongo_loader import load_browser_data
import datetime
from applogger import BotLog
import pandas as pd



class BranCollector:
    
    def __init__(self, metadata):
        print('inside init')
        self.metadata = metadata
        self.user = self.metadata['user']['user']
        self.db_user = self.metadata['db']['dbuser']
        self.db_pass = self.metadata['db']['dbpassword']
        self.db_uri = self.metadata['db']['uri']
        self.db_collectiondb = self.metadata['db']['collectiondb']
        self.db_collection = self.metadata['db']['collection']
        self.ge_arc_path = self.metadata['user']['data']['ge']['arc_path']
        self.gc_arc_path = self.metadata['user']['data']['gc']['arc_path']
        self.gc_profiles = self.metadata['user']['data']['gc']['profiles']
        self.logger_name = self.metadata['logger']['loggername']
        self.logger_handler = self.metadata['logger']['loghandler']
        self.logger_file = self.metadata['logger']['logfile']
        self.logger = BotLog(self.logger_file, self.logger_name, self.logger_handler).get_logger()
        self.logger.info('bran env loaded')

    def copy_file(self, src_file, dst_file):
        shutil.copy(src_file, dst_file)

    def move_file(self, src_file, dst_file):
        shutil.move(src_file, dst_file)


    def sqlite_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Exception as e:
            self.logger.error("load browser data exception occurred:", e)
        return conn
    
  
    def chrome_file(self):
        os.chdir(os.path.expanduser("~"))
        # create list of data files in profile path
        os.chdir(self.gc_profiles)
        data_files = [data_file for data_file in os.listdir(self.gc_profiles)]
        for file in data_files:
            self.logger.info('file {} extraction started'.format(file))
            try:
                history1 = sqlite3.connect(file)
            except Exception as e:
                self.logger.error("load browser data exception occurred:", e)
            h1 = history1.cursor()
            #sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
            sql_query = """SELECT urls.id id, urls.url url, urls.title title, urls.visit_count visit_count, 
                        urls.typed_count typed_count, urls.last_visit_time last_visit_time, urls.hidden hidden, 
                        visits.visit_time visit_time, visits.from_visit from_visit, visits.visit_duration visit_duration, 
                        visits.transition transition, visit_source.source source FROM urls JOIN visits ON 
                        urls.id = visits.url LEFT JOIN visit_source ON visits.id = visit_source.id"""

            h1.execute(sql_query)
            self.logger.info('chrome query {} executed'.format(sql_query))
            h1_data = h1.fetchall()
            h1.execute("select * from keyword_search_terms")
            h1_search = h1.fetchall()
            df_h1 = DataFrame(h1_data,columns=["id", "url", "title", "visit_count", "typed_count", "last_visit_time", "hidden", "visit_time","from_visit", "visit_duration","transition", "source"])
            df_h1['last_visit_time'] = df_h1['last_visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
            df_h1['visit_time'] = df_h1['visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))
            df_h1_search = DataFrame(h1_search, columns=["search_keyword_id", "search_url_id","search_term", "search_nterm"])
            h1.close()
            browsing_data = {'uid': self.user, 'layer':0, 'engine':'collector',
                             'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                             'data': {'search': json.loads(df_h1_search.T.to_json()),
                                      'history': json.loads(df_h1.T.to_json())}}
            load_browser_data([browsing_data])
            shutil.move(file, self.gc_arc_path)
            filename = file + '.json'
            with open(filename, 'a') as file:
                #print(sys_stats)
                data = browsing_data
                json.dump(data, file, default=str)
                file.close()
            shutil.move(filename, self.gc_arc_path)

    def chrome_export(self, export_file):
        with open(export_file) as f:
            data = json.loads(f.read())
            df_h1 = pd.DataFrame(data["Browser History"])
            df_h1 = df_h1.rename(columns={"time_usec": "last_visit_time", "page_transition": "transition", "client_id": "id"})
            df_h1['last_visit_time'] = df_h1['last_visit_time'].apply(lambda x: (datetime.datetime(1601, 1, 1) + datetime.timedelta(microseconds=x)).strftime('%Y-%m-%d %H:%M:%S'))

            #enrichment
            df_h1['source'] = 0
            df_h1['hidden'] = 0
            df_h1['visit_time'] = 0
            df_h1['visit_duration'] = 0
            df_h1['from_visit'] = 0
            df_h1['visit_count'] = 0
            df_h1['id'] = 0
            f.close()
        #print(df_h1.head(5))
        data_l1 = [{'username': 'sandy01011', 'element': 'login', 'origin': 'https://github.com/login', 'action': 'https://github.com/session', 'created_on': '2021-04-16 15:34:42', 'last_used': '2021-04-17 10:37:51'},
        {'username': 'sk2011mishra@gmail.com', 'element': 'username', 'origin': 'https://learn.upgrad.com/login', 'action': 'https://learn.upgrad.com/login', 'created_on': '2021-04-17 13:32:32', 'last_used': '2021-05-27 13:28:36'}, 
        {'username': '', 'element': '', 'origin': 'https://infinity.icicibank.com/', 'action': '', 'created_on': '2021-06-01 17:51:15', 'last_used': '1601-01-01 00:00:00'},
        {'username': 'bobbyojha333@gmail.com', 'element': 'email', 'origin': 'https://www.amazon.com/ap/signin', 'action': 'https://www.amazon.com/ap/signin', 'created_on': '2021-06-04 17:45:31', 'last_used': '2021-06-04 17:45:16'}]
        df_l1 = pd.DataFrame(data_l1)
        #print(df_l1.head(5))
        browsing_data = {'uid': self.user,'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'data': {'history': json.loads(df_h1.T.to_json()), 'login': json.loads(df_l1.T.to_json())}}

        filename = 'EnrichedBrowserHistory20211218.json'
        with open(filename, 'a') as file:
            #print(sys_stats)
            data = browsing_data
            json.dump(data, file, default=str)
            file.close()
        load_browser_data(self.db_collection,browsing_data)
