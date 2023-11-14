import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"

def get_person_data(id=None, URL=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(f'{id} : {data}')



get_person_data(id=1, URL=URL)
get_person_data(URL=URL)