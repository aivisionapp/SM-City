import os 
from dotenv import load_dotenv
load_dotenv()
import requests 
import json




api_key = os.getenv("SERVICE_ROLE")
url = os.getenv("API_URL")


table_name = "detection"

def select_all(table_name):
    querystring = {"select":"*"}
    headers = {
    "apikey": api_key,
    "Authorization": f"Bearer {api_key}"
    }
    response = requests.request("GET", f'{url}/{table_name}', headers=headers, params=querystring)
    # get json from response 
    response = response.json()
    return response

# print(select_all(table_name))


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


print(insert(table_name, {'class_name':'apple','image_data':'apple.jpg'}))



    













