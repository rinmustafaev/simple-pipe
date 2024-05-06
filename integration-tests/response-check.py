import requests
import os
import time
from urllib3.util import Retry
from requests.adapters import HTTPAdapter

WEBAPP_HOST= os.getenv('WEBAPP_HOST', 'localhost')
# Wait for server to start
# Define the retry strategy
retry_strategy = Retry(
    total=5,
    backoff_factor=2,
    status_forcelist=range(400, 599)
)
# Create an HTTP adapter with the retry strategy and mount it to session
adapter = HTTPAdapter(max_retries=retry_strategy)

# Create a session and mount the adapter
retry_session = requests.Session()
retry_session.mount(f'http://{WEBAPP_HOST}:8000', adapter)

response = retry_session.get(f'http://{WEBAPP_HOST}:8000/api/health')
response.raise_for_status()


response = requests.get(f'http://{WEBAPP_HOST}:8000/api/users')

if response.status_code != 200 and response.json() :
    raise Exception(f'Request failed with status code {response.status_code} and {response.json()}')

print('Response body:')
print(response.json())