import requests
import os

WEBAPP_HOST= os.getenv('WEBAPP_HOST', 'localhost')
response = requests.get(f'http://{WEBAPP_HOST}:8000/api/users')

if response.status_code != 200 and response.json() :
    raise Exception(f'Request failed with status code {response.status_code} and {response.json()}')

print('Response body:')
print(response.json())