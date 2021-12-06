# Objective
Analysing Browsing pattern can reveal many insights, our aim is to get a pattern to understand information clusters associated to a particular id.

## Data Collection

### Chrome Browser Collection Path

Location of Google Chrome history

Windows XP
C:\Documents and Settings\<username>\Local Settings\Application Data\Google\Chrome\User Data\Default
C:\Documents and Settings\<username>\Local Settings\Application Data\Google\Chrome\User Data\Default\Cache

Windows Vista, 7, 8, 10
C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default
C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\Cache

Mac OS X
/Users/<username>/Library/Application Support/Google/Chrome/Default
/Users/<username>/Library/Caches/Google/Chrome/Default/Cache

Linux/Unix
/home/<username>/.config/google-chrome/Default
/home/<username>/.cache/google-chrome/Default/Cache

####Format of Google Chrome history

#####Bookmarks
Chrome Bookmarks are stored in the 'Bookmarks' JSON file.

#####Cache
Chrome Cache is stored using an Index file ('index'), a number of Data Block files ('data_#'), and a number of separate data files ('f_######').

#####Cookies
Chrome Cookies are stored in the 'Cookies' SQLite database, within the 'cookies' table.

#####Downloads
Chrome Downloads are stored in the 'History' SQLite database, within the 'downloads' and 'downloads_url_chains' tables.

#####Favicons
Chrome Favicons are stored in the 'Favicons' SQLite database, within the 'favicons', 'favicon_bitmaps' and 'icon_mapping' tables. Older versions of Chrome stored Favicons in a 'Thumbnails' SQLite database, within the 'favicons' table.

#####Form History
Chrome Form History is stored in the 'Web Data' SQLite database, within the 'autofill' table. Older versions of Chrome stored associated dates within an 'autofill_dates' table.

#####Logins
Chrome Logins are stored in the 'Login Data' SQLite database, within the 'logins' table. Older versions of Chrome stored Logins in the 'Web Data' SQLite database.

#####Searches
Chrome Searches are stored in the 'History' SQLite database, within the 'keyword_search_terms' table. Associated URL information is stored within the 'urls' table.

#####Session Data
Chrome Session Data is stored in the 'Current Session', 'Current Tabs', 'Last Session' and 'Last Tabs' files.

#####Thumbnails
Chrome Thumbnails are stored in the 'Top Sites' SQLite database, within the 'thumbnails' table. Older versions of Chrome stored Thumbnails in a 'Thumbnails' SQLite database, within the 'thumbnails' table.

#####Website Visits
Chrome Website Visits are stored in the 'History' SQLite database, within the 'visits' table. Associated URL information is stored within the 'urls' table. Older versions of Chrome stored archived Website Visits in a separate 'Archived History' SQLite database, within the 'visits' table.

## ETL

RAW DATA---------> Extract -----> Transform -------> Load

## Data modeling

## Insights
