#Resource: https://realpython.com/python-api/

import requests

response = requests.get('https://bible-api.com/jn 3:16')
print(response.json())


# all interactions between a client—in this case your Python console—and an API are split into a request and a response:
    # Requests contain relevant data regarding your API request call, such as the base URL, the endpoint, the method used, the headers, and so on.
    # Responses contain relevant data returned by the server, including the data or content, the status code, and the headers.

#>>> response = requests.get("https://api.thedogapi.com/v1/breeds")
# response
#<Response [200]>
#>>> response.request
#<PreparedRequest [GET]>

#>>> request = response.request
#>>> request.url
#'https://api.thedogapi.com/v1/breeds'
#>>> request.path_url
#'/v1/breeds'
#>>> request.method
#'GET'
#>>> request.headers
#{'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate',
#'Accept': '*/*', 'Connection': 'keep-alive'}