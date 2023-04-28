import requests

BASE = "http://127.0.0.1:5000/"
# this is our base url

response = requests.put(BASE + "video/1/", {"likes": 10})
# this  {"likes": 10} is actually sent in a form so thats why we used print(request.form['likes'])
# which will return us the value 10
print(response.json())

""" the reason we are using json() is because we and this not to look like 
 a response object and to actually be some kind of information """



