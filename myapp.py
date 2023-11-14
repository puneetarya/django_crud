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



#get_person_data(id=1, URL=URL)
#get_person_data(URL=URL)
data = {
    'name':'Ravi',
    'roll':3,
    'city':'jhajjar'
}

def post_person_data(data, URL):

    json_data = json.dumps(data)
    r = requests.post(url = URL, data=json_data)
    response = r.json()
    print(response)

#post_person_data(data=data, URL=URL)

def update_person_data(data, URL):
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    response = r.json()
    print(response)

update_data = {
    'id' : 3,
    'name':'Ravi',
    'city':'Jhajjar'
}

#update_person_data(data=update_data, URL=URL)
delete_data = {'id':3}
def delete_person_data(data, URL):
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    response = r.json()
    print(response)

delete_person_data(delete_data, URL=URL)