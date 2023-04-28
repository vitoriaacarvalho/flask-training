import requests

BASE = "http://127.0.0.1:5000/"
# this is our base url

response = requests.post(BASE + "helloworld")
print(response.json())
""" the reason we are using json() is because we and this not to look like 
 a response object and to actually be some kind of information """



