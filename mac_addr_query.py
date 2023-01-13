import requests
import json
import re
import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv()
parser=argparse.ArgumentParser()
parser.add_argument("--addr", help="Mac Address")
args=parser.parse_args()

api_key = os.environ.get('API_KEY')
api_token = os.environ.get('API_TOKEN')
mac_address = args.addr

def validate_mac_address(mac_address:str) -> bool:
    """
    Validates the MAC address
    Returns true false

    mac_address: MAC address of device
    """
    pattern = r'^(([0-9a-fA-F]{2}[:]){5}([0-9a-fA-F]{2})|([0-9a-fA-F]{2}[-]){5}([0-9a-fA-F]{2})|[0-9a-fA-F]{12})$'
    return bool(re.match(pattern, mac_address))

def get_company_name(api_key:str, api_token:str, mac_address:str) -> str:
    """
    Queries company name of the MAC address
    Returns company name

    api_key: API Key for macaddress.io
    api_token: API Token for macaddress.io
    mac_address: MAC address of device
    """
    if not all([api_key, api_token, mac_address]):
        raise ValueError('Make sure that you pass all the variables')

    if not validate_mac_address(mac_address):
        raise ValueError('Enter a valid MAC address')
   
    url = f'https://api.macaddress.io/v1?apiKey={api_key}&output=json&search={mac_address}'

    headers = {
        'Authorization': f'Bearer {api_token}'
    }

    response = requests.get(url, headers=headers).json()
    if not 'vendorDetails' in response:
        raise ValueError('Couldn\'t get response from server')

    return response['vendorDetails'] ['companyName']

if __name__ == "__main__":
    company_name = get_company_name(api_key, api_token, mac_address)
    print(f'{company_name} - {mac_address}')