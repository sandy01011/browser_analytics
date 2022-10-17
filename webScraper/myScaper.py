# This file will contail all required functions to get webpage data

from bs4 import BeautifulSoup as bs
from bs4 import NavigableString, Tag
import re
import time
import json
import tabula
from tabula import read_pdf
from tabulate import tabulate
import socket
import logging
import os
import requests 

from datetime import datetime
timestamp = datetime.now().strftime("%Y%m%d%H%M")
log_path = os.getcwd() + os.mkdir('logs/')
log_file = 'logs/' + 'default' + '_' + timestamp + '.log'
soup_error_file = log_path + 'ongoingbids_soup_error' + timestamp
#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(filename=log_file, filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)


def gemSoup(url):
        logging.info(url)
        #logging.debug('type {} url {}'.format(type(url),url))
        try:
            #logging.debug('URL', url)
            page = requests.get(url)
        except Exception as exception:
            logging.error("First request Exception occurred", exc_info=True)
            time.sleep(9)
            try:
                #logging.debug('URL', url)
                page = requests.get(url)
            except Exception as exception:
                logging.error("Second request Exception occurred", exc_info=True)
        page_status = page.status_code   # if page try fails then page is referenced before assignment correct it
        if page_status == 200:
            logging.info("successfully loaded: ".format(url))
            soup = bs(page.content,'html.parser')
        else:
            logging.debug("{} loading failed with status code {}".format(url, page_status))
            soup = '0'
        encoding = page.encoding
        headers = page.headers
        soup = bs(page.content,'html.parser')
        return soup