import requests

base_url = "http://127.0.0.1:5000/"
payload = {'name':'jan','views':100,'likes':10}

response = requests.put(base_url+'video/'+str(0),params=payload)
print(response.json())

# input()
# response = requests.delete(base_url+'video/0')
# print(response.json())

