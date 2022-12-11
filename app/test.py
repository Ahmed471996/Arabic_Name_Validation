import requests 
import json

url = 'http://192.168.1.8:5000/predict'

data = {"message":"Ahmed"}

json_object = json.dumps(data, indent = 4)   
print(json_object)
response = requests.post(url,
                        json=json_object)
print(response.text)








