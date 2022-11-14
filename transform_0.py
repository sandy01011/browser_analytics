# This file will transform data
from mongo_loader import read_browser_data, update_layer

# read data
data_list = read_browser_data()
print(data_list)

# data cleaning, and composition
# remove dublicates

# EDA reports TimeSeries

# enrichment with doc_type (HTML,pdf,csv,vedio etc.) classfication and EDA enrichments
