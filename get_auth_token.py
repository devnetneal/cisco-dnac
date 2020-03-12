"""
A simple API call to get an authorisation token from Cisco DNA-C and print it

"""

import base64
import requests


def str_to_base64(input):
    b = base64.b64encode(input.encode())
    return b.decode()


url = "https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"

username = 'devnetuser'
password = 'Cisco123!'

unpwb64 = str_to_base64(username + ':' + password)
print(unpwb64)

payload = {}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic ' + unpwb64,
}

r = requests.request("POST", url, headers=headers, data=payload)

print(r.text)
print(r.status_code)
