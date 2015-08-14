# import urllib.request to use password manager, http handler and opener
import urllib.request

# import json to use javascript object notation to parse data that has been converted to string
import json

# set variables to connect to uTorrent web UI
port = 8080
url = "http://localhost:" + str(port) + "/gui/?list=1"
username = 'admin'
password = 'admin'
match = None

# initialize password manager, http handler and opener
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

# open URL to get data
request = opener.open(url)

# convert data to string in 'utf-8' format so can be converted to json
str_obj = request.read().decode('utf-8')

# parse json string and return json object using 'torrents' index to narrow object to just torrents
json_obj = json.loads(str_obj)['torrents']

# for each torrent in the json object, check if it is finished and delete if so
for torrent in json_obj:
    finished_parse = str(torrent).find("100.0 %")
    if finished_parse != -1:
        match = torrent[0].strip("'")
    if match != None:
        remove = opener.open("http://localhost:" + str(port) + "/gui/?action=remove&hash=" + match)
