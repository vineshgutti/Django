import requests
import json

# POST request
# d = {'name':'cpu','price':4500,'discount':500}
# print(type(d))
# print(json.dumps(d))
# print(type(json.dumps(d)))
# y = requests.post('http://127.0.0.1:8000/',data=json.dumps(d))

# GET request
# x = requests.get('http://127.0.0.1:8000/details')
# print(x.content)

# PUT request
# id=input()
# d = json.dumps({'name':'bike','price':100000,'discount':5000})
# r = requests.put('http://127.0.0.1:8000/update/'+id,data=d)
# # print(r.text)
# print(r.status_code)
# print(type(r.request.body))

# PATCH request
# id=input()
d={'name':'electric bike'}
e = requests.patch('http://127.0.0.1:8000/patch/'+"18",data=json.dumps(d))
print(e)
print(e.request.body)
print(type(e.request.body))

# Delete request
# id=input()
# x = requests.delete('http://127.0.0.1:8000/delete/'+id)
# print(x.text)