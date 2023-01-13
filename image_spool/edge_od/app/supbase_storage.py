import os 
from dotenv import load_dotenv
load_dotenv()
import requests 
import json


from storage3 import create_client


api_key = os.getenv("SERVICE_ROLE")
url = os.getenv("API_URL")

url = url 
key = api_key
headers = {"apiKey": key, "Authorization": f"Bearer {key}"}

storage_client = create_client(url, headers, is_async=False)

print(storage_client.list_buckets())







table_name = "detection"

def select_all(table_name):
    headers = {
    "apikey": api_key,
    "Authorization": f"Bearer {api_key}"
    }

    data = {}

    response = requests.request("GET", f'{url}/bucket', headers=headers)
    # get json from response 
   
    return response.status_code

print(select_all('detected-images'))


def insert(table_name, data):
    url = f'https://sxezeqnhhhwekcopfluw.supabase.co/rest/v1/{table_name}'
    payload = json.dumps(data)
    headers = {
    "apikey": api_key,
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "Prefer": "return=minimal"
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code


# print(insert(table_name, {'class_name':'apple','image_data':'apple.jpg'}))



    













