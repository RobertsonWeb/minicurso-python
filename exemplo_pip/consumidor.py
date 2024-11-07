import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.json())

print(response.json()['title'])

print(response.json()['completed'])