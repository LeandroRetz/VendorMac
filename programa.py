import requests
import re

url = "https://mac-address-lookup1.p.rapidapi.com/static_rapid/mac_lookup/"
mac_regex = r'[0-9a-fA-F]{2}(?:-[0-9a-fA-F]{2}){5}'
querystring = {"query":"0C:CC:47:E0:B8:6F"}

headers = {
    "x-rapidapi-key": "0660da2643mshdb18d19012bb7efp1dc26bjsn0181c3a07637",
    "x-rapidapi-host": "mac-address-lookup1.p.rapidapi.com"
}


with open('aaaa.txt','r') as arq:
    for line in arq:
        mac_addresses = re.findall(mac_regex, line)
        for mac in mac_addresses:
            print(mac)
            querystring = {"query":f"{mac}"}
            response = requests.get(url, headers=headers, params=querystring)
            response_json = response.json()
            if 'result' in response_json and len(response_json['result']) > 0:
                print(response_json['result'][0]['name'])
            else:
                print("Key 'name' not found in the response.")
