# import requests
import requests

# set variables to connect to uTorrent web UI
port = 8080
username = 'admin'
password = 'admin'

# set action urls
list_url = "http://localhost:{port}/gui/?list=1".format(port=port)
remove_url = "http://localhost:{port}/gui/?action=remove&hash={match}"

# open URL to get data
r = requests.get(list_url, auth=(username, password))

# return json object using 'torrents' index to narrow object to just torrents
json_obj = r.json()['torrents']

# for each torrent in the json object, check if it is finished and delete if so
for torrent in json_obj:
    finished_parse = str(torrent).find("100.0 %")
    if finished_parse != -1:
        match = torrent[0].strip("'")
        if match:
            remove = requests.get(remove_url.format(port=port, match=match),
                                  auth=(username, password))
