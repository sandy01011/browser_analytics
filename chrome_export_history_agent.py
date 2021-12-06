import json
#from pandas import DataFrame
import pandas as pd
from mongo_loader import load_browser_data
import datetime


bid = 'sk2011mishra@gmail.com'
with open("chrome_exported_browserhistory.json") as f:
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
browsing_data = {'bid': bid,'load_time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'data': {'history': json.loads(df_h1.T.to_json()), 'login': json.loads(df_l1.T.to_json())}}
load_browser_data('collection',browsing_data)

