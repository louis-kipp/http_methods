##GET is one of the most common HTTP methods you’ll use when working with REST APIs. 
# This method allows you to retrieve resources from a given API. GET is a read-only operation, 
# so you shouldn’t use it to modify an existing resource.

#To test out GET and the other methods in this section, you’ll use a service called JSONPlaceholder. 
# This free service provides fake API endpoints that send back responses that requests can process.

#Vitual env: python -m pip install requests
import requests

##API Endpoint: https://jsonplaceholder.typicode.com/todos/1

##GET
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())
print(response.status_code)

##POST
#Now, take a look at how you use requests to POST data to a 
# REST API to create a new resource. You’ll use JSONPlaceholder again, 
# but this time you’ll include JSON data in the request. Here’s the data that you’ll send:
api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()


##This code calls requests.get() to send a GET request to /todos/1, which responds with the todo 
# item with the ID 1. Then you can call .json() on the response object to view the data that came back from the API.
