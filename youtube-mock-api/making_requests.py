import requests

BASE = "http://127.0.0.1:5000/"
# this is our base url
"""data = [{"likes": 10, "name": "Tim", "views": 10000},
        {"likes": 112, "name": "Benji", "views": 22200},
        {"likes": 3, "name": "Alice", "views": 5}]

for i in range(len(data)):
    response = requests.post(BASE + "video/" + str(i), json=data[i])
    print(response.json())
"""


response = requests.get(BASE + "video/3")
print(response.json())

response = requests.delete(BASE + "video/1")
print(response)
input()
""" the reason we are using json() is because we and this not to look like 
 a response object and to actually be some kind of information """



