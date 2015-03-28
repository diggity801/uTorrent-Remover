import urllib.request
import json

url = "http://localhost:8080/gui/?list=1"
port = 8080
username = 'admin'
password = 'admin'
match = None

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, url, username, password)
handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

request = opener.open(url)
string = request.read().decode('utf-8')
json_obj = json.loads(string)['torrents']

for torrent in json_obj:
    finished_parse = str(torrent).find("100.0 %")
    if finished_parse != -1:
        match = torrent[0].strip("'")
    if match != None:
        remove = opener.open("http://localhost:" + port + "/gui/?action=remove&hash=" + match)
